# Author: JD 09/30/2021

hight = int(input("Hight:"))

weight = int(input("Weight: "))

bmi = weight / (hight ** 2)

if bmi < 19:
    print("Underweight")
elif bmi < 25:
    print("Healthy")
elif bmi < 30:
    print("Overweight")
elif bmi < 40:
    print("Obese")
else:
    print("Extremly Obese")