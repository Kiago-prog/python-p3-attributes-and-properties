#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # Validate and set name
        if name is not None:
            if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
                return
            else:
                self.name = name.title()
        else:
            self.name = None

        # Validate and set job
        if job is not None:
            if job not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                return
            else:
                self.job = job
        else:
            self.job = None
