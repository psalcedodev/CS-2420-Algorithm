import sys
from datetime import datetime, date, time, timezone
import bst
from colors import *


class Student:

    def __init__(self, first, last, ssn, email, age):
        self.mFirst = first
        self.mLast = last
        self.mSsn = ssn
        self.mEmail = email
        self.mAge = age

    def __eq__(self, rhs):
        if self.mSsn == rhs.mSsn:
            return True
        else:
            return False

    def __lt__(self, rhs):
        if self.mSsn < rhs.mSsn:
            return True
        else:
            return False

    def __gt__(self, rhs):
        if self.mSsn > rhs.mSsn:
            return True
        else:
            return False

    def getAge(self):
        return self.mAge


def InsertNames():
    lines = open("./InsertNamesMedium.txt", "r").readlines()
    start = datetime.now()
    students = bst.BST()
    failures = 0
    for line in lines:
        data = line.split()
        student = Student(data[0], data[1], data[2], data[3], data[4])
        if not students.insert(student):
            failures += 1
    end = datetime.now()
    time = end.timestamp() - start.timestamp()
    prCyan('====================================')
    prMagenta("Inserting")
    prCyan('====================================')
    prYellow("time of insertion: %s seg" % round(time, 2))
    prGreen("Success: %s" % students.getSize())
    prRed("Failures: %s" % failures)

    return students


gTOTAL_AGE = 0


def addAges(s):
    global gTOTAL_AGE
    gTOTAL_AGE += int(s.getAge())


def deleteNames(students):
    start = datetime.now()
    lines = open("./DeleteNamesMedium.txt", "r").readlines()
    start = datetime.now()
    success = 0
    failures = 0
    for line in lines:
        data = line.strip()
        dummy_student = Student(0, 0, data, 0, 0)
        if not students.delete(dummy_student):
            failures += 1
        else:
            success += 1
    end = datetime.now()
    time = end.timestamp() - start.timestamp()
    prCyan('====================================')
    prMagenta("Deleting")
    prCyan('====================================')
    prYellow("Time of deletion: %s seg" % round(time, 2))
    prGreen("success: %s" % success)
    prRed("failures %s" % failures)


def retrieveNames(students):
    lines = open("./RetrieveNamesMedium.txt", "r").readlines()
    start = datetime.now()
    totalAge = 0
    totalStudents = 0
    failures = 0
    for line in lines:
        data = line.strip()
        dummy = Student(0, 0, data, 0, 0)
        studentR = students.retrieve(dummy)
        if studentR is None:
            failures += 1
        else:
            totalAge += int(studentR.mAge)
            totalStudents += 1
    avgAge = totalAge / totalStudents
    end = datetime.now()
    time = end.timestamp() - start.timestamp()
    prCyan('====================================')
    prMagenta("Retrieving")
    prCyan('====================================')
    prYellow("time of retrieval: %s seg" % round(time, 2))
    prGreen("success: %s" % totalStudents)
    prRed("failures: %s" % failures)
    prCyan("avg age: %s" % avgAge)


def traverseNames(students):
    start = datetime.now()
    students.traverse(addAges)
    avg_age = gTOTAL_AGE / students.getSize()
    end = datetime.now()
    time = end.timestamp() - start.timestamp()
    prCyan('====================================')
    prMagenta("Traversing")
    prCyan('====================================')
    prYellow("Time of traversal: %s seg" % round(time, 2))
    prCyan("Avg Age: %s" % avg_age)


def print_items(item):
    print(item.mSsn)


def main():
    students = InsertNames()
    deleteNames(students)
    retrieveNames(students)
    traverseNames(students)


if __name__ == "__main__":
    main()
