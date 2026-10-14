"""manage application functions and operations"""
from datetime import date

class Application_Manager:
    def __init__(self):
        self.applications = []
        self.next_id = 1

    def update_next_id(self):
        """Update the next_id based on the highest application ID in the list."""
        if self.applications:
            self.next_id = max(job.application_id for job in self.applications) + 1
        else:
            self.next_id = 1

    def add_application(self, application):
        """Add a new application to the list."""
        application.application_id = self.next_id
        self.next_id += 1
        self.applications.append(application)

    def remove_application(self, application_ID):
        """Remove an application by its ID."""
        for job in self.applications:
            if job.application_id == application_ID:
                self.applications.remove(job)
                print(
                    f"Application with ID {application_ID} has been removed.")
                return
        print(f"Application with ID {application_ID} not found.")

    def get_application(self, application_ID):
        """Retrieve an application by its ID."""
        for job in self.applications:
            if job.application_id == application_ID:
                return job
        print(f"Application with ID {application_ID} not found.")

    def list_applications(self):
        """List all applications."""
        return self.applications

    def update_application(self, application_ID, updates):
        """Update an existing application with new values."""
        application = self.get_application(application_ID)
        if application is None:
            print(f"Application with ID {application_ID} not found.")
            return
        allowed_fields = [
            "company", "position", "job_type", "location", "contact",
            "status", "applied_date", "interview_date", "url", "notes"]

        for field, value in updates.items():
            if field in allowed_fields:
                setattr(application, field, value)
                setattr(application, "updated_date", date.today().isoformat())
            else:
                print(f"Field '{field}' is not allowed for update.")
        return True

    