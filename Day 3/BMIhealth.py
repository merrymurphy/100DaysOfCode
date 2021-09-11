# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=weight/(height*height)
print(f"{weight}/({height}*{height})={BMI}")

if BMI<28.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif (BMI>=18.5) and (BMI<25):
  print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI<30:
  print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI<35:
  print(f"Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinicaly obese")




