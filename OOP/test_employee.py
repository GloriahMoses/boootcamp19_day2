import unittest
from employee import Person, Student, StaffMember, Lecturer, SubodinateStaff 

class StudentTestCases(unittest.TestCase):
  
  def setUp(self):
    self.S = Student(1245, "undergraduate", "gloriah","moses",23467)
    
  def tearDown(self):
    del self.S

  def test_Student_is_instance_of_Person(self):
    self.assertTrue(isinstance(self.S, Person), msg='Student is not a subclass of Person')
  
  def test_Student_can_enroll_course(self):
    course = self.S.enrol_course("Computer Science")
    self.assertEquals(course, "You have successfully enrolled")
  
  def test_Student_can_change_course(self):
    message = self.S.change_course("Computer Science","Literature")
    self.assertEquals(message, "You are not enrolled to any course")
  


class StaffMemberTestCases(unittest.TestCase):

  def setUp(self):
    self.SM = StaffMember(245, "Casual", "Library", "gloriah","moses",23467)
    
  def tearDown(self):
    del self.SM

  def test_StaffMember_is_instance_of_Person(self):

    self.assertTrue(isinstance(self.SM, Person), msg='StaffMember is not a subclass of Person')
      



class LecturerTestCases(unittest.TestCase):
  
  def setUp(self):
    self.L = Lecturer(45, 245, "Casual", "Library", "gloriah","moses",23467)
    
  def tearDown(self):
    del self.L
  
  def tes_Lecturer_is_instance_of_Person(self):
    self.assertTrue(isinstance(self.L, Person), msg='Lecturer is not a subclass of Person')

  def test_Lecturer_can_assign_course(self):
    course = self.L.assign_course("Computer Science")
    self.assertEquals(course, "successfully assigned course")



class SubodinateStaffTestCases(unittest.TestCase):
  
  def setUp(self):
    self.SS = SubodinateStaff(72, 245, "Casual", "Library", "gloriah","moses",23467)
    
  def tearDown(self):
    del self.SS
  
  def tes_SubodinateStaff_is_instance_of_Person(self):
    self.assertTrue(isinstance(self.SS, Person), msg='SubodinateStaff is not a subclass of Person')

  def test_Lecturer_can_assign_station(self):
    station = self.SS.assign_station("Library Counter")
    self.assertEquals(station, "Staff assigned work station successfully")
  

if __name__ == "__main__":
  unittest.main()