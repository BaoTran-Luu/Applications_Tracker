"""Manage application data storage and retrieval."""
import json
from .job_application import JobApply

def save_applications_to_file(applications, filename):
    """Save the list of applications to a file."""
    data = [job.to_dict() for job in applications]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_applications_from_file(filename):
    """Load the list of applications from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [JobApply.from_dict(job_data) for job_data in data] 
    except FileNotFoundError:
        return []