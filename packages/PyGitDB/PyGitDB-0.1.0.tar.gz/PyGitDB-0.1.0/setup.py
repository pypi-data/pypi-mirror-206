"""
Project setup
"""
import os

from setuptools import find_namespace_packages, find_packages, setup


def get_long_description():
    root = os.path.dirname(__file__)
    with open(os.path.join(root, "README.md")) as f:
        description = f.read()
    return description


base_requirements = {
    "pydantic",
    "duckdb",
    "duckdb-engine",
    "requests",
    "loguru",
    "pandas",
    "SQLAlchemy~=1.4",
}

dev = {"isort", "pre-commit", "ruff", "black", "pycln"}

setup(
    name="PyGitDB",
    version="0.1.0",
    description="Load git stats into a DuckDB db locally for easy analytics.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    zip_safe=True,
    include_package_data=True,
    packages=find_namespace_packages(),
    entry_points={
        "console_scripts": ["gitdb = gitdb.main:cli"],
    },
    install_requires=list(base_requirements),
    extras_require={
        "dev": list(dev),
    },
)
