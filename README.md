Database Validation Framework (Python + PostgreSQL + PyTest)

This project implements a database validation framework designed to test and verify the integrity of a PostgreSQL database. It covers schema validation, data quality checks, and business rule validation using Python, SQL, and PyTest.
It is intended to demonstrate skills relevant to Technical Software Test Engineer, SDET, and QA Automation roles.

The framework connects to a PostgreSQL database, loads a test schema and seed data, and executes automated validation tests. All tests run inside GitHub Actions using a PostgreSQL service container.

Features
Schema Validation

The framework verifies that the database structure matches expected definitions, including:

Required tables exist.

Required columns are present with correct data types.

Primary and foreign key constraints exist.

Unique and non-null constraints are enforced.

Data Quality Validation

Data quality checks confirm that:

Critical fields contain no null values.

Duplicate values do not exist where uniqueness is expected.

Numeric fields contain valid and positive values.

Referential integrity is respected across tables.

Business Rule Validation

Tests include simple examples of business logic checks, such as:

All customers must have at least one order.

Order items must contain valid quantities and product references.

Project Structure
database-validation-python/
├─ src/
│  ├─ db/
│  │  ├─ config.py
│  │  ├─ client.py
│  │  └─ queries.py
│  └─ validation/
│     ├─ rules_schema.py
│     ├─ rules_data_quality.py
│     └─ rules_business.py
├─ sql/
│  ├─ create_schema.sql
│  └─ seed_data.sql
├─ tests/
│  ├─ conftest.py
│  ├─ test_schema_validation.py
│  ├─ test_data_quality.py
│  └─ test_business_rules.py
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ requirements.txt
├─ README.md
└─ .env.example

Technology Stack

Python 3.11

PostgreSQL

PyTest

psycopg2

GitHub Actions (CI)

How It Works

GitHub Actions starts a PostgreSQL service container.

Environment variables from the CI pipeline configure the test database.

PyTest loads the schema using create_schema.sql.

Seed data is inserted using seed_data.sql.

Validation tests are executed:

Schema tests

Data quality tests

Business logic tests

A detailed HTML test report is generated.

Running Tests Locally
1. Install dependencies
pip install -r requirements.txt

2. Start a local PostgreSQL instance

You may use Docker:

docker run -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  postgres:16

3. Set environment variables

Copy .env.example to .env and adjust if needed.

4. Run the tests
pytest --html=report.html --self-contained-html

Continuous Integration (GitHub Actions)

The CI workflow:

Starts PostgreSQL

Installs dependencies

Applies schema and seed data

Executes all tests

Produces test reports

This ensures the entire framework works in an isolated, reproducible environment.

Purpose of the Project

This repository demonstrates practical skills used in database testing and backend QA automation:

Building database-driven test frameworks

Executing automated SQL-based validations

Working with PyTest fixtures

Using GitHub Actions for CI

Understanding schema and data consistency checks

Using PostgreSQL and SQL for data verification

It is part of a larger portfolio of automation engineering projects.