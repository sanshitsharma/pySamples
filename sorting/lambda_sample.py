#!/usr/bin/python

class Student(object):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grades(self):
        return 'CBA'.index(self.grade) / float(self.age)

if __name__ == "__main__":
    student_objects = [Student("anshu", 4.0, 31), Student('Ruhi', 3.5, 33), Student('ANU', 3.9, 27)]
    sObjs = sorted(student_objects, key = lambda student: student.grade)
    print student_objects
    print sObjs
