import csv
import json
import os

import requests
from dotenv import load_dotenv


BASE_URL = "https://jsonplaceholder.typicode.com/users"


def process_employees():
    employees = []

    with open("employees.csv", "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            row["salary"] = int(row["salary"])
            employees.append(row)

    with open("employees.json", "w", encoding="utf-8") as json_file:
        json.dump(employees, json_file, indent=4)

    high_earners = [
        employee for employee in employees if employee["salary"] > 50000
    ]

    with open("high_earners.csv", "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = employees[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(high_earners)

    print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")


def get_users():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        users = response.json()
    except requests.exceptions.Timeout:
        print("The users request timed out.")
        return
    except requests.exceptions.ConnectionError:
        print("Could not connect to the users API.")
        return

    saved_users = []
    for user in users[:3]:
        print(f"{user.get('id')} - {user.get('name')} - {user.get('email')}")
        address = user.get("address", {})
        saved_users.append(
            {
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "city": address.get("city"),
            }
        )

    with open("users.json", "w", encoding="utf-8") as json_file:
        json.dump(saved_users, json_file, indent=4)


def check_missing_user():
    try:
        response = requests.get(f"{BASE_URL}/9999", timeout=5)
        if response.status_code == 404:
            print("/users/9999 -> 404 Not found")
        else:
            response.raise_for_status()
            print(f"/users/9999 -> {response.status_code}")
    except requests.exceptions.Timeout:
        print("The /users/9999 request timed out.")
    except requests.exceptions.ConnectionError:
        print("Could not connect to check /users/9999.")


def main():
    load_dotenv()
    if not os.getenv("API_KEY"):
        raise RuntimeError("API_KEY is missing from .env")

    process_employees()
    get_users()
    check_missing_user()


if __name__ == "__main__":
    main()
