import numpy as np

class Student:
    def __init__(self, student_id: str, name: str, dob: str):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, course_credits: dict):
        if not self.marks:
            self.gpa = 0.0
            return self.gpa
        
        marks_list = []
        weights_list = []
        for course_id, mark in self.marks.items():
            if course_id in course_credits:
                marks_list.append(mark)
                weights_list.append(course_credits[course_id])
                
        if len(marks_list) == 0 or sum(weights_list) == 0:
            self.gpa = 0.0
        else:
            self.gpa = float(np.average(np.array(marks_list), weights=np.array(weights_list)))
        return self.gpa