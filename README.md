# Refactoring Project

Please do not fork this repository. Use it as a template for your refactoring project. Create pull requests in your own repository even if you are working alone, and mark the completed checkboxes with an `x` in the pull request message.

## Project Hub

This repository now includes three main entry points:

- [README.md](./README.md): setup instructions and project navigation
- [project-for-today.md](./project-for-today.md): the assignment brief
- [King-County.ipynb](./King-County.ipynb): the notebook used for the refactoring task

If you want to explore the optional stretch goal, there is also a working reference implementation in [bonus_solution/](./bonus_solution/).

## Repository Guide

- `King-County.ipynb`: the original notebook with EDA, cleaning, feature engineering, and modeling
- `project-for-today.md`: the required tasks and stretch goals
- `bonus_solution/`: a small FastAPI + Postgres + Docker reference solution for the optional CRUD task
- `requirements.txt`: notebook dependencies for the main project

## Setup

The notebook dependencies are listed in [requirements.txt](./requirements.txt). You can install them with the following commands.

### `macOS`

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### `Windows`

For `PowerShell`:

```powershell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For `Git-Bash`:

```text
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Suggested Workflow

1. Read the assignment brief in [project-for-today.md](./project-for-today.md).
2. Work through the notebook in [King-County.ipynb](./King-County.ipynb).
3. Refactor the cleaning and feature-engineering logic into Python files.
4. Build a reusable pipeline.
5. If you want to go further, use [bonus_solution/](./bonus_solution/) as a reference for the optional FastAPI + Docker stretch goal.

## Bonus Solution

The [bonus_solution/](./bonus_solution/) folder contains a minimal working example of:

- a FastAPI CRUD API
- Postgres persistence
- a Dockerfile for the API
- a `docker-compose.yml` file to run the API and database together

It is included as a reference implementation for the optional stretch task, not as a required project structure.
