class Entity:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_info(self):
        return self.__name, self.__id

    def __str__(self):
        return self.__name


class Student(Entity):
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.__dob = dob

    def show_student(self):
        a, b = super().get_info()
        return a, b, self.__dob


class Course(Entity):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__marks = {}

    def input_mark(self, sid, mark):
        self.__marks.update({sid: mark})

    def show_mark(self):
        for i in self.__marks:
            print(f"Student id {i}:{self.__marks[i]}")
        return

    def show_course(self):
        a, b = super().get_info()
        return a, b


class List:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self, stu):
        self.__students.append(stu)

    def add_course(self, cour):
        self.__courses.append(cour)

    def show_students(self):
        for i in self.__students:
            name, id, dob = i.show_student()
            print(f"Student ID {id}: {name}")

    def show_courses(self):
        for i in self.__courses:
            name, id = i.show_course()
            print(f"Course ID {id}: {name}")

    def add_mark(self,cid,sid,mark):
        a = 0
        for i in self.__courses:
            name, id = i.show_course()
            if id == cid:
                i.input_mark(sid,mark)
                a += 1
                print("Mark added")
                break
        if a == 0:
            print("There is no such course or student id")

    def show_mark(self,cid):
        a = 0
        for i in self.__courses:
            name, id = i.show_course()
            if id == cid:
                a += 1
                i.show_mark()
                break
        if a == 0:
            print("There is no such course")


database = List()
while True:
    print("""Please choose an option below:
    0. Exit
    1. List all students
    2. List all courses
    3. Add mark
    4. Show marks of a course
    5. Add students
    6. Add course""")
    selection = input()
    if selection == "0":
        break
    elif selection == "1":
        database.show_students()
    elif selection == "2":
        database.show_courses()
    elif selection == "3":
        mark_info = input("Enter the id of the course, the id and mark of the student").split()
        database.add_mark(mark_info[0],mark_info[1],mark_info[2])
    elif selection == "4":
        cid = input("Enter the id of the course")
        database.show_mark(cid)
    elif selection == "5":
        num_students = int(input("Please enter the number of new students: "))
        for i in range(num_students):
            student_info = input(f"Enter the Name, ID, DoB of student #{i + 1}: ").split()
            database.add_student(Student(student_info[0], student_info[1], student_info[2]))
    elif selection == "6":
        num_courses = int(input("Please enter the number of new courses: "))
        for i in range(num_courses):
            course_info = input(f"Enter the Name, ID of course #{i + 1}: ").split()
            database.add_course(Course(course_info[0], course_info[1]))
    else:
        print("Invalid selection. Please try again.")
