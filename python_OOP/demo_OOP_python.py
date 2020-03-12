class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


hang = Student(Student.POSTGRADUATE, "hang", "nguyen", "20161384")
hang.enrol("K61_toan_tin")
print('name: '+hang.name)
print('POSTGRADUATE'+str(hang.POSTGRADUATE))
print('class: '+ str(hang.classes))

ngoc = Lecturer(StaffMember.PERMANENT, "ngoc", "chile", "123456789")
ngoc.assign_teaching("deep_learning")
print(ngoc.name)
print(ngoc.courses_taught)