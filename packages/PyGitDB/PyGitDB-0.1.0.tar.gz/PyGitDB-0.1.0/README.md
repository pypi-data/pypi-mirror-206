# Git DB

**Making sense of GitHub projects is harder than it should be.**

1. Default `insights` are poor and do give us much information on how the project is evolving.
2. The API model is not straightforward (issues & PRs are handled together, some calls are easier on v3 than v4,...).
3. The typical approach consists on reading the API and computing metrics on-the-fly. 
   This is too strict and new insights have a high cost (API calls).

Our goal with **Git DB** is to focus on simplicity and flexibility:
- We dump all the project's data to a local [Duck DB](https://duckdb.org/).
- Your answers are one SQL query away.

## Installation

```bash
pip install PyGitDB
```

## What will you find?

### stargazers

| Column Name | Type      |
|-------------|-----------|
| id          | INTEGER   |
| starred_at  | TIMESTAMP |
| user_id     | INTEGER   |
| user_login  | VARCHAR   |

### issues

| Column Name        | Type      |
|--------------------|-----------|
| id                 | INTEGER   |
| number             | INTEGER   |
| title              | VARCHAR   |
| body               | VARCHAR   |
| user_id            | INTEGER   |
| user_login         | VARCHAR   |
| state              | VARCHAR   |
| assignees          | VARCHAR[] |
| labels             | VARCHAR[] |
| created_at         | TIMESTAMP |
| updated_at         | TIMESTAMP |
| closed_at          | TIMESTAMP |
| author_association | VARCHAR   |
| html_uri           | VARCHAR   |

### pulls

| Column Name         | Type      |
|---------------------|-----------|
| id                  | INTEGER   |
| number              | INTEGER   |
| title               | VARCHAR   |
| body                | VARCHAR   |
| user_id             | INTEGER   |
| user_login          | VARCHAR   |
| state               | VARCHAR   |
| assignees           | VARCHAR[] |
| labels              | VARCHAR[] |
| created_at          | TIMESTAMP |
| updated_at          | TIMESTAMP |
| merged_at           | TIMESTAMP |
| closed_at           | TIMESTAMP |
| author_association  | VARCHAR   |
| html_uri            | VARCHAR   |

### contributors

| Column Name   | Type      |
|---------------|-----------|
| id            | INTEGER   |
| contributions | INTEGER   |
| user_id       | INTEGER   |
| user_login    | VARCHAR   |

### latest_reviews

| Column Name  | Type      |
|--------------|-----------|
| id           | INTEGER   |
| number       | INTEGER   |
| reviewer     | VARCHAR   |
| review_state | VARCHAR   |
| reviewed_at  | TIMESTAMP |

### weekly_commits

| Column Name  | Type      |
|--------------|-----------|
| id           | INTEGER   |
| date         | TIMESTAMP |
| commits      | INTEGER   |

## How to run

### 1. CLI

Once installed, you can prepare the database for your GitHub project directly with the CLI:

```bash
❯ gitdb --help                                                                                                                                                                                                                                                                                                                                                                 х INT Py 3.9.13 11:36:05
usage: gitdb [-h] [-r REPO] [-o OWNER] [-f FILE] [--clean]

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Repo to analyze
  -o OWNER, --owner OWNER
                        Repo owner
  -f FILE, --file FILE  Db file path
  --clean               Clean the existing db
```

For example:

```bash
❯ gitdb -r OpenMetadata -o open-metadata                                                                                                                                                                                                                                                                                                                                          3s Py 3.9.13 11:37:04
2023-05-01 11:38:01.472 | INFO     | gitdb.main:init:30 - Starting GitDB in gitdb.db...
2023-05-01 11:38:01.473 | INFO     | gitdb.api.client:__init__:45 - Preparing client with root='api.github.com' owner='open-metadata' repo='OpenMetadata' token=SecretStr('**********') start_date='Aug 1 2021' timeout=300 graphql='graphql'
2023-05-01 12:31:29.240 | INFO     | gitdb.dao.core:process:36 - Starting to process ReviewsDAO...
2023-05-01 12:31:29.240 | INFO     | gitdb.dao.core:process:36 - Starting to process IssuesDAO...
2023-05-01 12:31:29.241 | INFO     | gitdb.dao.core:process:36 - Starting to process StarsDAO...
2023-05-01 12:31:29.241 | INFO     | gitdb.dao.core:process:36 - Starting to process WeeklyCommitsDAO...
2023-05-01 12:31:29.241 | INFO     | gitdb.dao.core:process:36 - Starting to process ContributorsDAO...
2023-05-01 12:31:44.356 | INFO     | gitdb.main:init:54 - Loaded all data in 0.26767790695000004 min.
```

### 2. Run from Python

If instead, you want to call the database generation from another Python program, you can use the following:

```python
from gitdb.main import init

session = init(
   repo=...,
   owner=...,
   token=...,
   path=...,
)
```

The `init` method will create the Duck DB database and will give you the `SQLAlchemy` Session to start running
your queries.

## Examples

Connect to the database using `duckdb` and start running queries:

```python
import duckdb

conn = duckdb.connect(database="gitdb.db", read_only=True)
conn.execute("show tables").fetchall()
```

A typical question is wanting to see the evolution of the stars by week. This can be achieved with the
following query:

```sql
WITH CTE AS (
   SELECT 
       strftime(starred_at - INTERVAL (DAYOFWEEK(starred_at) - 1) DAY, '%Y/%m/%d') as starred_week,
       count(id) as stars 
   from stargazers 
   group by strftime(starred_at - INTERVAL (DAYOFWEEK(starred_at) - 1) DAY, '%Y/%m/%d')
)
select
   starred_week as week,
   SUM(stars) over (ORDER BY starred_week ASC) as stars_by
FROM CTE
ORDER BY starred_week ASC
```

## How does this work?

We are running a bunch of calls against the GitHub API when dumping all the data against the db. Doing this sequentially
can be rather long. Our `client` has a `get_all_parallel` function that accepts a number of threads as a parameter to do calls
in parallel by playing with totals and pagination.

The big chunk of work has gone into preparing the `init` call to be as fast as possible by leveraging multithreading in the host.
