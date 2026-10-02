#insert dictionary
students = {
    "01" :{
        "name" : "tuan",
        "age" : 19,
        "Dob": "30/10/2007",
            "classs" :{
            "python" : 2.0,
            "c" : 3.5
        }

    },
    "02" : {
        "name" : "huy",
        "age" : 19,
        "Dob" : "21/3/2007",
        "classs":{
            "python" : 3.0,
            "c" : 3.5
        }
    }
}


#create a function to search for id
def search_student(student_id):

    if student_id in students:
      student = students[student_id]
      print(student["name"])
      print(student["age"])
      print(student["Dob"])
      for classes, grade in student["classs"].items():
        print(classes,":",grade)

    else:
      print("invalid id")

def student_infos(student_info):

    if student_info in students:
      student1 = students[student_info]
      print(student1["name"])
      print(student1["age"])
      print(student1["Dob"])
    else:
      print("invalid id")

#run everytime
while True:

  print("1.mark info")
  print("2.student info")
  print("3.out")

  test = input("pick option")
  if test == "1":
    student_id = input("your student id")
    search_student(student_id)

  elif test == "2":
    student_info = input("your student id")
    student_infos(student_info)

  else:
    print("goodbye")
    break




