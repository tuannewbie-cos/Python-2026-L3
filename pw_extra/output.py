def display_menu():
    print("\n" + "=" * 40)
    print(" === STUDENT MARK MANAGEMENT (PW4) ===")
    print("=" * 40)
    print("1. Input Students")
    print("2. Input Courses")
    print("3. Input Marks for Course")
    print("4. List Students (Sorted by GPA)")
    print("5. Exit")
    print("=" * 40)

def display_students(students, courses):
    print("\n" + "=" * 45)
    print("        === STUDENT LIST (Sorted by GPA) ===")
    print("=" * 45)
    
    course_credits = {c.id: c.credit for c in courses}
    for s in students:
        s.calculate_gpa(course_credits)

    sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
    
    if not sorted_students:
        print("No student data available.")
        return

    print(f"{'ID':<10} {'Name':<20} {'GPA':<10}")
    print("-" * 45)
    for s in sorted_students:
        print(f"{s.id:<10} {s.name:<20} {s.gpa:<10.2f}")
    print("=" * 45)