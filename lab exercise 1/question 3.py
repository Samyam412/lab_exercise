""" N students take K apples and distribute them among each other evenly. The remaining
(the Indivisible) part remains in the basket. How many apples will each single student
get? How many apples will remain in the basket? The program reads the numbers N and
K. It should print the two answers for the questions above """

apples = int(input("enter the number of apples: "))
students = int(input("enter the number of students: "))

apples_for_students = apples//students

apples = apples% students
print(f"The students get {apples_for_students} apples and {apples} apples remain in the basket")
