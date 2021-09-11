# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number)) #direct input always inputs as string
# 🚨 Don't change the code above 👆
num=str(two_digit_number) 
x=int(num[0])
y=int(num[1])
####################################
#Write your code below this line 👇
print(x+y)