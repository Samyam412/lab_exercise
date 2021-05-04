""" Solve each of the following problems using Python Scripts. Make sure you use appropriate
variable names and comments. When there is a final answer have Python print it to the
screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2
"""


mass = float(input("enter your weight in kg:"))
height = float(input("enter your height in meters:"))
BMI = mass / (height * height)

print(f"Your BMI is {BMI}")
