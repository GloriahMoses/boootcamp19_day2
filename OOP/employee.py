class Person(object):
    
    def __init__(self, first_name, second_name, ID_number):
        self.first_name = first_name
        self.second_name = second_name
        self.ID_number = ID_number


class Student(Person):

    def __init__(self, admission_id, student_type,*args, **kwargs):
        self.student_type = student_type
        self.courses = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol_course(self, course):
        self.courses.append(course)
        return "You have successfully enrolled"

    def change_course(self, current_course, new_course):
        if len(self.courses)>0:
            key = 0
            for course in self.courses:
                if course==current_course:
                    self.courses[key]=new_course
                key+=1
            return "You have successfully change the course"    
        else:
            return "You are not enrolled to any course"            

class StaffMember(Person):

    def __init__(self, employee_number, employment_type, department, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):

    def __init__(self, lecturer_number, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_course(self, course):
        self.courses_taught.append(course)
        return "successfully assigned course"


class SubodinateStaff(StaffMember):
    
    def __init__(self, staff_number, *args, **kwargs):
        self.work_stations = []
        super(SubodinateStaff, self).__init__(*args, **kwargs)

    def assign_station(self, work_station):
        self.work_stations.append(work_station)
        return "Staff assigned work station successfully"    
class Person(object):
    
    def __init__(self, first_name, second_name, ID_number):
        self.first_name = first_name
        self.second_name = second_name
        self.ID_number = ID_number


class Student(Person):

    def __init__(self, admission_id, student_type,*args, **kwargs):
        self.student_type = student_type
        self.courses = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol_course(self, course):
        self.courses.append(course)
        return "You have successfully enrolled"

    def change_course(self, current_course, new_course):
        if len(self.courses)>0:
            key = 0
            for course in self.courses:
                if course==current_course:
                    self.courses[key]=new_course
                key+=1
            return "You have successfully change the course"    
        else:
            return "You are not enrolled to any course"            

class StaffMember(Person):

    def __init__(self, employee_number, employment_type, department, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):

    def __init__(self, lecturer_number, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_course(self, course):
        self.courses_taught.append(course)
        return "successfully assigned course"


class SubodinateStaff(StaffMember):
    
    def __init__(self, staff_number, *args, **kwargs):
        self.work_stations = []
        super(SubodinateStaff, self).__init__(*args, **kwargs)

    def assign_station(self, work_station):
        self.work_stations.append(work_station)
        return "Staff assigned work station successfully"    
