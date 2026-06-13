# Summative M4

A simple command-line project management tool implemented in Python.

## What it does

- Loads project, task, and user data from JSON files in the `data/` folder.
- Provides a menu-based CLI to:
  - add, edit, and delete users
  - add, edit, and delete projects
  - add tasks to projects
  - list projects and tasks
- Persists changes back to the same JSON files when saving or exiting.

## How to run

From the repository root:

```bash
python3 main.py
```

## Data storage

- `data/projects.json` stores project records
- `data/tasks.json` stores task records
- `data/users.json` stores user records

The program reads these files at startup and writes them back when saving.

## Notes

- The CLI is defined in `services/admin.py`.
- The data model helpers live in `models/project.py`, `models/task.py`, and `models/user.py`.
- The program has been verified to compile and run basic add/load operations.
