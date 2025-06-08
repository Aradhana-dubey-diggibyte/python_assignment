from collections import namedtuple

def average_marks(n, columns, data):
    Student = namedtuple('Student', columns)
    marks = [int(Student(*row).MARKS) for row in data]
    return round(sum(marks) / n, 2)
