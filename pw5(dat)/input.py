# pw6/input.py
import math

def input_student_info():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    dob = input("Enter Date of Birth (DD/MM/YYYY): ").strip()
    return student_id, name, dob

def input_course_info():
    course_id = input("Enter Course ID: ").strip()
    name = input("Enter Course Name: ").strip()
    credit = float(input("Enter Credits: "))
    return course_id, name, credit

def input_mark(student_id: str, course_id: str):
    raw_mark = float(input(f"Enter mark for Student ID {student_id} in Course ID {course_id}: "))
    return math.floor(raw_mark * 10) / 10