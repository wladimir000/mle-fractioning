# Refactoring Project

Please **use this repository as a template** for your refactoring project. Create pull requests in your own repository even if you are working alone, and use them to track the work you complete.

## Project Hub

This repository includes three main entry points:

- [README.md](./README.md): setup instructions and project navigation
- [project-for-today.md](./project-for-today.md): the assignment brief
- [King-County.ipynb](./King-County.ipynb): the notebook used for the refactoring task

If you want to explore the optional stretch goal, there is also a working reference implementation in [bonus_solution/](./bonus_solution/).

## Repository Guide

- `King-County.ipynb`: the original notebook with EDA, cleaning, feature engineering, and modeling
- `project-for-today.md`: the required tasks and stretch goals
- `bonus_solution/`: a small FastAPI + Postgres + Docker reference solution for the optional CRUD task
- `requirements.txt`: notebook dependencies for the main project

The notebook includes a modeling section as well. For the core project, you only need to refactor the data cleaning and feature engineering parts, but the modeling cells show how those processed features are used later in a machine learning workflow.

## Environment

Please set up a new virtual environment. You can use the following commands:

### `macOS`

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### `Windows`

For `PowerShell` CLI:

```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For `Git-Bash` CLI:

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The [requirements.txt](requirements.txt) file contains all libraries and dependencies needed to execute the notebook.

## Suggested Workflow

1. Read the assignment brief in [project-for-today.md](./project-for-today.md).
2. Work through the notebook in [King-County.ipynb](./King-County.ipynb).
3. Refactor the cleaning and feature engineering logic into Python files.
4. Build a reusable pipeline.
5. If you want an extra challenge, extend your refactor to cover the modeling step as well.
6. If you want to go further, use [bonus_solution/](./bonus_solution/) as a reference for the optional FastAPI + Docker stretch goal.

## Bonus Solution

The [bonus_solution/](./bonus_solution/) folder contains a minimal working example of:

- a FastAPI CRUD API
- Postgres persistence
- a `Dockerfile` for the API
- a `docker-compose.yaml` file to run the API and database together

It is included as a reference implementation for the optional stretch task, not as a required project structure.
