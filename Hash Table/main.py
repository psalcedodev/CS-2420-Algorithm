import sys
from datetime import datetime, date, time, timezone
import hash
from colors import *


class Student:

    def __init__(
        self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
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

    def __int__(self):
        return int(self.mSsn.replace('-', ''))

    def getAge(self):
        return self.mAge

def insertNames():
    lines = open('./InsertNamesMedium.txt').readlines()
    start = datetime.now()
    students = hash.UUC(3000000)
    failures = 0
    for line in lines:
        data = line.split()
        student = Student(data[0], data[1], data[2], data[3], data[4])
        if students.insert(student) == False:
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
    lines = open('./DeleteNamesMedium.txt').readlines()
    start = datetime.now()
    success = 0
    failures = 0
    for line in lines:
        data = line.strip()
        dummy_student = Student(0, 0, data, 0, 0)
        if students.delete(dummy_student) == False:
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
    lines = open('./RetrieveNamesMedium.txt').readlines()
    start = datetime.now()
    total_age = 0
    total_students = 0
    failures = 0
    for line in lines:
        data = line.strip()
        dummy = Student(0, 0, data, 0, 0)
        studentR = students.retrieve(dummy)
        if studentR:
            total_age += int(studentR.getAge())
            total_students += 1
        else:
            failures += 1
    avg_age = total_age / total_students
    end = datetime.now()
    time = end.timestamp() - start.timestamp()
    prCyan('====================================')
    prMagenta("Retrieving")
    prCyan('====================================')
    prYellow("time of retrieval: %s seg" % round(time, 2))
    prGreen("success: %s" % total_students)
    prRed("failures: %s" % failures)
    prCyan("avg age: %s" % avg_age)


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


def main():
    students = insertNames()
    deleteNames(students)
    retrieveNames(students)
    traverseNames(students)

if __name__ == '__main__':
    main()
