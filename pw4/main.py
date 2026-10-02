from domains.student import Student
from domains.course import Course
from input import input_student_info, input_course_info, input_mark
from output import display_menu, display_students

students = []
courses = []

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            num = int(input("How many students to add? ").strip())
            for _ in range(num):
                sid, name, dob = input_student_info()
                students.append(Student(sid, name, dob))
                
        elif choice == '2':
            num = int(input("How many courses to add? ").strip())
            for _ in range(num):
                cid, cname, credit = input_course_info()
                courses.append(Course(cid, cname, credit))
                
        elif choice == '3':
            if not students or not courses:
                print("\n[!] Please input students and courses first!")
                continue
            
            cid = input("Enter Course ID to input marks for: ").strip()
            course_found = any(c.id == cid for c in courses)
            if not course_found:
                print(f"\n[!] Course ID '{cid}' not found!")
                continue
                
            course_credits = {c.id: c.credit for c in courses}
            
            for s in students:
                print(f"\n--- Student: {s.name} ({s.id}) ---")
                mark = input_mark()
                s.marks[cid] = mark
                s.calculate_gpa(course_credits)
                
        elif choice == '4':
            display_students(students, courses)
            
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\n[!] Invalid choice, please enter 1-5.")

if __name__ == "__main__":
    main()