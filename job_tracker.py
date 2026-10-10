"""Job Application Tracker - a simple command-line app.

Run with:  python job_tracker.py
Data is saved in applications.json next to the script.
"""

import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("applications.json")
STATUSES = ["applied", "interview", "offer", "rejected"]


# ---------- Saving and loading ----------

def load_applications():
    """Read applications from the JSON file (empty list if none yet)."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_applications(applications):
    """Write all applications to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(applications, f, indent=2)


# ---------- Helpers ----------

def ask_number(prompt, maximum):
    """Ask for a number between 1 and maximum. Returns None if invalid."""
    answer = input(prompt).strip()
    if answer.isdigit() and 1 <= int(answer) <= maximum:
        return int(answer)
    print("Invalid number.")
    return None


def show_applications(applications, status_filter=None):
    """Print applications as a numbered list."""
    if not applications:
        print("\nNo applications yet.")
        return

    print(f"\n{'#':<4}{'Company':<20}{'Position':<25}{'Status':<12}{'Date'}")
    print("-" * 70)
    for i, app in enumerate(applications, start=1):
        if status_filter and app["status"] != status_filter:
            continue
        print(
            f"{i:<4}{app['company']:<20}{app['position']:<25}"
            f"{app['status']:<12}{app['date_applied']}"
        )
        if app["notes"]:
            print(f"    Notes: {app['notes']}")


# ---------- Actions ----------

def add_application(applications):
    company = input("Company: ").strip()
    position = input("Position: ").strip()
    if not company or not position:
        print("Company and position are required.")
        return

    applications.append({
        "company": company,
        "position": position,
        "status": "applied",
        "date_applied": str(date.today()),
        "notes": input("Notes (optional): ").strip(),
    })
    save_applications(applications)
    print("Application added.")


def update_status(applications):
    show_applications(applications)
    if not applications:
        return
    number = ask_number("\nWhich application? (number): ", len(applications))
    if number is None:
        return

    print("Statuses:", ", ".join(STATUSES))
    new_status = input("New status: ").strip().lower()
    if new_status not in STATUSES:
        print("Unknown status.")
        return

    applications[number - 1]["status"] = new_status
    save_applications(applications)
    print("Status updated.")


def delete_application(applications):
    show_applications(applications)
    if not applications:
        return
    number = ask_number("\nDelete which application? (number): ", len(applications))
    if number is None:
        return

    removed = applications.pop(number - 1)
    save_applications(applications)
    print(f"Deleted {removed['company']} - {removed['position']}.")


def show_summary(applications):
    print("\nSummary")
    print("-" * 20)
    for status in STATUSES:
        count = sum(1 for app in applications if app["status"] == status)
        print(f"{status.capitalize():<12}{count}")
    print(f"{'Total':<12}{len(applications)}")


# ---------- Main loop ----------

def main():
    applications = load_applications()

    while True:
        print("\n=== Job Application Tracker ===")
        print("1. Add application")
        print("2. List all applications")
        print("3. Filter by status")
        print("4. Update status")
        print("5. Delete application")
        print("6. Summary")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            show_applications(applications)
        elif choice == "3":
            status = input(f"Status ({', '.join(STATUSES)}): ").strip().lower()
            if status in STATUSES:
                show_applications(applications, status_filter=status)
            else:
                print("Unknown status.")
        elif choice == "4":
            update_status(applications)
        elif choice == "5":
            delete_application(applications)
        elif choice == "6":
            show_summary(applications)
        elif choice == "7":
            print("Good luck with your applications!")
            break
        else:
            print("Please choose 1-7.")


if __name__ == "__main__":
    main()
