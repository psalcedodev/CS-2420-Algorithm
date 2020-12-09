import time

# Color text


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


class Student:
    def __init__(self, fname, lname, ssn, email, age):
        self.fname = fname
        self.lname = lname
        self.ssn = ssn
        self.email = email
        self.age = age


def main():
    time_started = time.time()
    students = []
    duplicates = 0
    lines = open("./InsertNames.txt", "r").readlines()
    total_lines = len(lines)
    for i in range(total_lines):
        split_line = lines[i].split()
        new_student = Student(
            split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])

        for student in students:
            if student.ssn == new_student.ssn:
                duplicates += 1
                prRed("[DUPLICATE FOUND]")
                print("[Student]: %s %s\n[SSN] => %s" %
                      (new_student.fname, new_student.lname, new_student.ssn))
                duplicatedStudent = new_student.fname, new_student.lname
                continue
        students.append(new_student)
    time_elapsed = (time.time() - time_started)
    print()
    print("Duplicated Students: %s\nTime Elapsed: %s\n" %
          (duplicates, float(time_elapsed)))


if __name__ == "__main__":
    main()
