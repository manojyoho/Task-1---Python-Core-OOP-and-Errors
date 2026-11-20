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

## NumPy, Pandas, and Matplotlib task

The analytics exercise has its own employee data, including two missing
salaries and one duplicate row. From the project folder, run:

```powershell
.\.venv\Scripts\python.exe analytics\analytics_task.py
```

The script fills missing salaries with the median, removes duplicates,
summarizes departments, performs inner/left/outer joins, and saves four charts
as PNG files in `analytics\charts`.

The console shows only the requested summary:

```text
Student averages: [85.   81.33 88.67 80.  ]
Headcount: Sales 2 | HR 2 | IT 3 | Finance 1
Outer join: department with no employees listed: Marketing
```

Chart insights:
- Bar: Finance has the highest average salary.
- Histogram: Salaries range from 48000 to 90000.
- Scatter: Employee 5 has the highest salary.
- Line: Salary reaches its maximum at employee 5.