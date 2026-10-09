import math

def input_student_info():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    dob = input("Enter Date of Birth (DD/MM/YYYY): ").strip()

    # text
    with open("students.txt", "a") as f:
        f.write(f"{student_id},{name},{dob}\n")

    return student_id, name, dob


def input_course_info():
    course_id = input("Enter Course ID: ").strip()
    name = input("Enter Course Name: ").strip()
    credit = float(input("Enter Credits: "))

    with open("courses.txt", "a") as f:
        f.write(f"{course_id},{name},{credit}\n")

    return course_id, name, credit


def input_mark(student_id: str, course_id: str):
    raw_mark = float(input(f"Enter mark for Student ID {student_id} in Course ID {course_id}: "))

    mark = math.floor(raw_mark * 10) / 10

    with open("marks.txt", "a") as f:
        f.write(f"{student_id},{course_id},{mark}\n")

    return mark