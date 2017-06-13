class StaffMember():

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