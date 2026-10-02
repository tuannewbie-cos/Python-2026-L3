import math
import numpy as np


class Student:

  def __init__(self, student_id, name, dob):
    self.id = student_id
    self.name = name
    self.dob = dob
    self.marks = {}  # {course_id: mark}
    self.gpa = 0.0

  def calculate_gpa(self, courses):
    if not self.marks:
      self.gpa = 0.0
      return self.gpa

    marks_list = []
    credits_list = []

    for course_id, mark in self.marks.items():
      if course_id in courses:
        marks_list.append(mark)
        credits_list.append(courses[course_id].credits)

    if not marks_list:
      self.gpa = 0.0
      return self.gpa

    # Convert to numpy arrays
    np_marks = np.array(marks_list)
    np_credits = np.array(credits_list)

    # Calculate weighted GPA using numpy.average
    self.gpa = float(np.average(np_marks, weights=np_credits))
    return self.gpa


class Course:

  def __init__(self, course_id, name, credits):
    self.id = course_id
    self.name = name
    self.credits = credits


class StudentManagementSystem:

  def __init__(self):
    self.students = []
    self.courses = {}

  def input_students(self):
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
      print(f"\n--- Student {i+1} ---")
      s_id = int(input("Student ID: "))
      name = input("Student Name: ")
      dob = input("Date of Birth (DoB): ")
      self.students.append(Student(s_id, name, dob))

  def input_courses(self):
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
      print(f"\n--- Course {i+1} ---")
      c_id = input("Course ID: ")
      name = input("Course Name: ")
      credits = float(input("Credits: "))
      self.courses[c_id] = Course(c_id, name, credits)

  def input_marks(self):
    if not self.courses or not self.students:
      print("\n[!] Please enter students and courses first!")
      return

    c_id = input("\nEnter Course ID to input marks for: ")
    if c_id not in self.courses:
      print("[!] Course not found!")
      return

    print(f"\nInputting marks for course: {self.courses[c_id].name}")
    for student in self.students:
      raw_mark = float(input(f"Enter mark for {student.name} ({student.id}): "))

      # Round-down score to 1-digit decimal using math.floor
      floored_mark = math.floor(raw_mark * 10) / 10
      student.marks[c_id] = floored_mark

  def sort_students_by_gpa(self):
    """Calculates all GPAs and sorts students in descending order."""
    for student in self.students:
      student.calculate_gpa(self.courses)

    # Sort descending by GPA
    self.students.sort(key=lambda s: s.gpa, reverse=True)

  def display_students(self):
    if not self.students:
      print("\n[!] No students in database.")
      return

    self.sort_students_by_gpa()

    print("\n" + "=" * 55)
    print("      STUDENT LIST (Sorted by GPA Descending)")
    print("=" * 55)
    print(f"{'ID':<10} {'Name':<20} {'DoB':<12} {'GPA':<5}")
    print("-" * 55)

    for s in self.students:
      print(f"{s.id:<10} {s.name:<20} {s.dob:<12} {s.gpa:.2f}")
    print("=" * 55)

  def run(self):
    while True:
      print("\n=== STUDENT MANAGEMENT SYSTEM ===")
      print("1. Input Students")
      print("2. Input Courses")
      print("3. Input Marks for Course")
      print("4. Display Students (Sorted by GPA)")
      print("5. Exit")

      choice = input("Choose an option (1-5): ")

      if choice == "1":
        self.input_students()
      elif choice == "2":
        self.input_courses()
      elif choice == "3":
        self.input_marks()
      elif choice == "4":
        self.display_students()
      elif choice == "5":
        print("Exiting system. Goodbye!")
        break
      else:
        print("Invalid choice, please try again.")


if __name__ == "__main__":
  system = StudentManagementSystem()
  system.run()