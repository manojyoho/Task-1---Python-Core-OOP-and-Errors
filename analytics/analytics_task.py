from pathlib import Path
from io import StringIO

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")

import matplotlib.pyplot as plt


DATA_FOLDER = Path(__file__).parent
EMPLOYEES_FILE = DATA_FOLDER / "employees.csv"
DEPARTMENTS_FILE = DATA_FOLDER / "departments.csv"
CHART_FOLDER = DATA_FOLDER / "charts"


def show_marks_analysis():
    marks = np.array(
        [
            [78, 85, 92],
            [88, 76, 80],
            [90, 91, 85],
            [70, 82, 88],
        ]
    )

    _marks_shape = marks.shape
    student_averages = marks.mean(axis=1)
    _subject_averages = marks.mean(axis=0)
    print("Student averages:", np.round(student_averages, 2))

    marks_with_grace = marks + 5
    weights = np.array([0.40, 0.35, 0.25])
    _weighted_scores = np.dot(marks_with_grace, weights)


def load_and_clean_employees():
    employees = pd.read_csv(EMPLOYEES_FILE)

    # Keep the required Pandas exploration quiet so only summary lines print.
    employees.info(buf=StringIO())
    _description = employees.describe()
    _first_employee = employees.loc[0, ["name", "department"]]
    _second_employee = employees.iloc[1]
    _high_salary_employees = employees.loc[
        employees["salary"] > 50000, ["name", "department", "salary"]
    ]

    missing_salary_count = employees["salary"].isna().sum()
    duplicate_count = employees.duplicated().sum()

    employees["id"] = pd.to_numeric(employees["id"]).astype(int)
    employees["salary"] = pd.to_numeric(employees["salary"], errors="coerce")
    employees = employees.drop_duplicates().copy()

    median_salary = employees["salary"].median()
    employees["salary"] = employees["salary"].fillna(median_salary).astype(int)

    return employees


def show_department_analysis(employees):
    departments = pd.read_csv(DEPARTMENTS_FILE)

    department_summary = employees.groupby("department").agg(
        headcount=("id", "count"),
        average_salary=("salary", "mean"),
        maximum_salary=("salary", "max"),
    )

    department_order = ["Sales", "HR", "IT", "Finance"]
    headcount_text = " | ".join(
        f"{department} {department_summary.loc[department, 'headcount']}"
        for department in department_order
    )
    print("Headcount:", headcount_text)

    inner_join = pd.merge(employees, departments, on="department", how="inner")
    left_join = pd.merge(employees, departments, on="department", how="left")
    outer_join = pd.merge(employees, departments, on="department", how="outer")

    no_employee_departments = outer_join.loc[
        outer_join["id"].isna(), "department"
    ].drop_duplicates()
    print(
        "Outer join: department with no employees listed: "
        + ", ".join(no_employee_departments)
    )
    return department_summary


def save_charts(employees, department_summary):
    CHART_FOLDER.mkdir(exist_ok=True)
    department_order = ["Sales", "HR", "IT", "Finance"]

    average_salary = department_summary.reindex(department_order)["average_salary"]
    plt.bar(average_salary.index, average_salary, label="Average salary")
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FOLDER / "average_salary_by_department.png")
    plt.close()

    plt.hist(employees["salary"], bins=5, label="Employee salaries")
    plt.title("Employee Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of employees")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FOLDER / "salary_histogram.png")
    plt.close()

    plt.scatter(
        employees["id"],
        employees["salary"],
        label="Employees",
        color="darkorange",
    )
    plt.title("Salary by Employee ID (Scatter)")
    plt.xlabel("Employee ID")
    plt.ylabel("Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FOLDER / "salary_scatter.png")
    plt.close()

    plt.plot(
        employees["id"],
        employees["salary"],
        marker="o",
        label="Salary",
        color="green",
    )
    plt.title("Salary by Employee ID (Line)")
    plt.xlabel("Employee ID")
    plt.ylabel("Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FOLDER / "salary_line.png")
    plt.close()


def main():
    show_marks_analysis()
    employees = load_and_clean_employees()
    department_summary = show_department_analysis(employees)
    save_charts(employees, department_summary)


if __name__ == "__main__":
    main()
