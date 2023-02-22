courses = {}
tudents = {}
dob = {}
marks = []


def total_student():
    a = int(input("Enter the total number of student: "))
    return a


def student_info():
    Id = input("Enter the student id: ")
    name = input("Enter the student's name: ")
    DOB = input("Enter the student's DOB: ")
    students.update({Id: name})
    dob.update({Id: DOB})


def total_course():
    a = int(input("Enter the total number of courses: "))
    return a


def course_info():
    Id = input("Enter course id: ")
    name = input("Enter course name: ")
    courses.update({Id: name})


def student_mark():
    cid = input("Enter the course id: ")
    sid = input("Enter the student id: ")
    mark = input("Enter the student's mark: ")
    marks.append([cid, sid, mark])


def list_course():
    for i in courses:
        print("Course:", courses[i])
        print("ID:", i)


def list_student():
    for i in students:
        print("Student's name:", students[i])
        print("ID:", i)
        print("Student's DOB:", dob[i])


def show_mark_course():
    cid = input("Enter course id: ")
    for i in marks:
        if i[0] == cid:
            print("Student's name:", students[i[1]])
            print("Student's mark:", i[2])


while True:
    print("\nWhat do you want to do?")
    print("1. Input students'infos")
    print("2. Input courses'infos")
    print("3. Input student's mark")
    print("4. List out courses")
    print("5. List out students")
    print("6. List out marks of a course")
    opt = input()
    if opt == "1":
        for i in range(total_student()):
            student_info()
    elif opt == "2":
        for i in range(total_course()):
            course_info()
    elif opt == "3":
        student_mark()
    elif opt == "4":
        list_course()
    elif opt == "5":
        list_student()
    elif opt == "6":
        show_mark_course()
    else:
        print("Please only enter a number from 1 to 6!")
