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
    def _init_(self,name="",job="default"):
        self._name=name
        self._job=job
    
    @property 
    def get_name(self):
        return self._name.title()

    @property 
    def get_job(self):
        return self._job



    
    def set_name(self, name):
        if len(name) < 1 or len(name) > 25:
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value 

    
    def set_job(self,job):
        if job not in APPROVED_JOBS:
            print( "Job must be in list of approved jobs.")
        else:
            self._job = job  
   name = property(get_name, set_name)

    
   

person=Person()

