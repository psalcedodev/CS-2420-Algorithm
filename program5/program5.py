import time

from colors import *


class Student:
    def __init__(self, fname, lname, ssn, email, age):
        self.fname = fname
        self.lname = lname
        self.ssn = ssn
        self.email = email
        self.age = age


def insertNames(students):
    time_started = time.time()
    duplicates = []
    lines = open("./InsertNames.txt", "r").readlines()
    total_lines = len(lines)
    for i in range(total_lines):
        split_line = lines[i].split()
        new_student = Student(
            split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])
        for student in students:
            if student.ssn == new_student.ssn:
                duplicates.append(new_student)
                continue
        students.append(new_student)
        time_elapsed = (time.time() - time_started)

    for student in duplicates:
        prMagenta("%s %s " % (student.fname, student.lname))
    prYellow("Time Elapsed: %s segs" %
             (int(time_elapsed)))

# Traverse all students in the pythonList, and print their average age (as a Float, not an Int). Print how many seconds that took.


def getAge(students):
    avg_age = 0
    total_students = len(students)
    time_started = time.time()
    for i in range(total_students):
        avg_age += float(students[i].age)
    avg_age /= total_students
    time_elapsed = (time.time() - time_started)
    prMagenta("Average age: %s" % "{:.2f}".format(avg_age))
    prYellow("Time Elapsed: %s segs" % int(time_elapsed))


def deleteNames(students):
    time_started = time.time()
    dellines = open('./DeleteNames.txt', 'r').readlines()
    deleted = 0
    notfound = []
    for i in range(len(dellines)):
        social = dellines[i][:-1]
        matched = False
        start = 0
        while start < len(students):
            if students[start].ssn == social:
                students.pop(start)
                deleted += 1
                matched = True
                break
            else:
                start += 1

        if not matched:
            notfound.append(social)

    time_elapsed = (time.time() - time_started)
    prYellow("SSN not found: %s" % (notfound))
    prYellow("Time Elapsed: %s segs" % int(time_elapsed))


def retrieveNames(students):
    time_started = time.time()
    retlines = open('./RetrieveNames.txt', 'r').readlines()
    retrieved = 0
    notfound = []
    avg_age = 0
    for i in range(len(retlines)):
        social = retlines[i][:-1]
        matched = False
        for student in students:
            if student.ssn == social:
                matched = True
                retrieved += 1
                avg_age += float(student.age)
                break
        if not matched:
            notfound.append(social)
    avg_age /= retrieved
    time_elapsed = (time.time() - time_started)
    prYellow("SSN not found: %s" % (notfound))
    prMagenta("Average age: %s" % "{:.2f}".format(avg_age))
    prYellow("Time Elapsed: %s segs" % int(time_elapsed))


def main():
    students = []
    prCyan('====================================')
    prGreen('Running Names')
    prCyan('--------------------')
    insertNames(students)
    prCyan('====================================')
    prGreen('Running Average Age')
    prCyan('--------------------')
    getAge(students)
    prCyan('====================================')
    prGreen('Deleting Students in DeleteNames.txt')
    prCyan('--------------------')
    deleteNames(students)
    prCyan('====================================')
    prGreen('Retrieving Students in RetrieveNames.txt')
    prCyan('--------------------')
    retrieveNames(students)


if __name__ == "__main__":
    main()
