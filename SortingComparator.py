from functools import cmp_to_key

# This is sample program to use user-defined comparator method for a Class in Python3.x
# Python3.x require cmp_to_key to convert a function to key argument of sorted function.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return '%s %d' % (self.name, self.marks)

    def comparator(a, b):
        if a.marks > b.marks:
            return -1
        elif a.marks == b.marks:
            if a.name >= b.name:
                return 1
            else:
                return -1
        else:
            return 1


n = int(input())
data = []
for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    student = Student(name, marks)
    data.append(student)

data = sorted(data, key=cmp_to_key(Student.comparator))
for i in data:
    print(i.name, i.marks)