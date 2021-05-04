""" A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
The program should read three integers: the number of students in each of the three
classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10
desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough for the third group of 22 students. So, we need 32 desks in total."""

students_a = int(input("enter the number of students in class a:"))
students_b = int(input("enter the number of students in class b:"))
students_c = int(input("enter the number of students in class c:"))

def desk(std):
    desk_needed = std // 2
    if std % 2 != 0:
        desk_needed += 1
    return desk_needed

desk_a = desk(students_a)
desk_b = desk(students_b)
desk_c = desk(students_c)

total_desk = desk_a + desk_b + desk_c

print(f" The desk needed in class 1 with {students_a} students is {desk_a} \n The desk needed in class 2 with {students_b} students is {desk_b} \n The desk needed in class 3 with {students_c} students is {desk_c} \n The total number of desks needed is {total_desk}")