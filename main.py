import json
FILE = "jobs.json"
def load_jobs():
    try:
        with open(FILE, "r") as f:
            return json.load(f) 
    except (FileNotFoundError, json.JSONDecodeError):
        return []        
def save_jobs(jobs):
    with open(FILE, "w") as f:
        json.dump(jobs, f, indent=4)
def add_job():
    company = input("Enter company name:")
    role = input("Enter role:")
    job = {"company": company, "role": role, "status": "Applied"}
    jobs = load_jobs()
    jobs.append(job)
    save_jobs(jobs)
    print("Job added successfully")
def view_jobs():
    jobs = load_jobs()
    if not jobs:
        print("No jobs found")
        return
    print("\n Your Job Applications:\n")
    for i, job in enumerate(jobs):
        print(f"{i + 1}. {job['company']}-{job['role']}[{job['status']}]")
def update_status():
    jobs = load_jobs()
    view_jobs()
    if not jobs:
        return
    try:
        index = int(input("Enter job number to update:")) - 1
        if index < 0 or index >= len(jobs):
            print("Invalid number")
            return
        print("1. Applied\n2. Interview\n3. Rejected\n4. Offer")
        choice = input("Enter new status:")
        status_map = {"1": "Applied", "2": "Interview", "3": "Rejected", "4": "Offer"}
        if choice not in status_map:
            print("Invalid choice. Status not updated.")
            return
        jobs[index]["status"] = status_map[choice]
        save_jobs(jobs)
        print("Status updated")
    except ValueError:
        print("Error occurred")

def delete_jobs():
    jobs = load_jobs()
    view_jobs()
    if not jobs:
        return
    try:
        index = int(input("Enter job number to delete:")) - 1
        if index < 0 or index >= len(jobs):
            print("Invalid number")
            return
        jobs.pop(index)
        save_jobs(jobs)
        print("job is deleted")
    except ValueError:
        print("Error occurred")
def search_job():
    keyword = input("Enter company or role to search: ").lower()
    jobs = load_jobs()
    found = False
    for job in jobs:
        if keyword in job["company"].lower() or keyword in job["role"].lower():
            print(f"{job['company']} - {job['role']} [{job['status']}]")
            found = True
    if not found:
        print("No matching jobs found")
def main():
    while True:
        print("\n-----JOB TRACKER-----")
        print("1.ADD JOB")
        print("2.VIEW JOB")
        print("3.UPDATE STATUS")
        print("4.DELETE JOB")
        print("5.SEARCH JOB")
        print("6.EXIT")
        choice = input("Enter choice: ")
        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_jobs()
        elif choice == "5":
            search_job()
        elif choice == "6":
            print("THANKYOU")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
