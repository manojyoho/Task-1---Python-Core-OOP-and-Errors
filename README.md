# Task-1---Python-Core-OOP-and-Errors
Python Core, OOP and Errors
Test 

## Employee CSV and API task

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set your API key in `.env`, then run:

```powershell
python data_task.py
```

The script reads `employees.csv`, creates `employees.json` and
`high_earners.csv`, prints details for the first three API users, and saves
their names, emails, and address cities to `users.json`.