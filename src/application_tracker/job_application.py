""" define JobApply class with attributes and methods to manage job applications """

from datetime import datetime, date


class JobApply:

   
    def __init__(self, company, position, job_type, location, contact, status, applied_date,  interview_date, url, notes):
        self.company = company
        self.position = position.title()
        self.job_type = JobApply.valid_job_type(job_type) # fulltime, parttime, minijob, werkstudent
        self.location = location
        self.contact = contact.title()
        self.status = JobApply.valid_status(status) #applied, online assignment, techinical test, interview, offer, rejected, withdrawn
        self.applied_date = JobApply.valid_date(applied_date, "applied_date")
        self.updated_date = date.today().isoformat() # Update the updated_date when the application is created or modified
        self.interview_date = JobApply.valid_date(interview_date, "interview_date") # could take None if not scheduled yet
        self.url = url
        self.notes = notes



    def to_dict(self):
        """Convert the JobApply instance to a dictionary."""
        return {
            "company": self.company,
            "position": self.position,
            "job_type": self.job_type,
            "location": self.location,
            "contact": self.contact,
            "status": self.status,
            "applied_date": self.applied_date.isoformat() if self.applied_date else None,
            "updated_date": self.updated_date.isoformat() if isinstance(self.updated_date, date) else self.updated_date,
            "interview_date": self.interview_date.isoformat() if self.interview_date else None,
            "url": self.url,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        """Create a JobApply instance from a dictionary."""
        return cls(
            company=data.get("company"),
            position=data.get("position"),
            job_type=data.get("job_type"),
            location=data.get("location"),
            contact=data.get("contact"),
            status=data.get("status"),
            applied_date=data.get("applied_date"),
            interview_date=data.get("interview_date"),
            url=data.get("url"),
            notes=data.get("notes")
        )


    JOB_TYPES = ["vollzeit", "teilzeit", "minijob", "werkstudent", "praktikum"]
    STATUSES = ["research","applied", "online assignment", "technical test", "interview",
                 "offer", "rejected", "withdrawn"]

    @staticmethod
    def valid_job_type(job_type):
        """Validate the job type. Accepts predefined job types."""
        job_type = job_type.lower()
        if job_type in JobApply.JOB_TYPES:
            return job_type
        else:
            raise ValueError(f"Invalid job type '{job_type}'. Expected one of: {', '.join(JobApply.JOB_TYPES)}.")

    @staticmethod
    def valid_status(status):
        """Validate the application status. Accepts predefined statuses."""
        status = status.lower()
        if status in JobApply.STATUSES:
            return status
        else:
            raise ValueError(f"Invalid status '{status}'. Expected one of: {', '.join(JobApply.STATUSES)}.")

    @staticmethod
    def valid_date(date_str, field_name):
        """Validate the date format. Accepts 'YYYY-MM-DD' format."""
        if date_str is None:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format '{date_str}' for field '{field_name}'. Expected format: YYYY-MM-DD.")

    