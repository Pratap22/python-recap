# Mutable Default Parameters - Bad Idea

class Student:
  def __init__(self, name="", grades=None): #Very Bad Idea
    self.name = name
    self.grades = grades or []

  def take_exam(self, result):
    self.grades.append(result)


pratap = Student("Pratap")
raju = Student()
pratap.take_exam(70)
print(pratap.grades)
print(raju.grades)
print(raju.name)
print(pratap.name)

