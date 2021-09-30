# Author: JD 09/30/2021

hight = int(input("Hight:"))

weight = int(input("Weight: "))

bmi = weight / (hight ** 2)

if bmi < 19:
    print("Underweight")
elif bmi < 25:
    print("Healthy")
