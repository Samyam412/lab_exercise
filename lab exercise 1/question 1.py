
#Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
num = []
sum = 0
for i in range(3):
    number = int(input("enter a number - "))
    i = number
    num.append(i)

for i in range(len(num)):
    sum = sum+ num[i]

print(sum)
