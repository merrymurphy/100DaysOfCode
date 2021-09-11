print("Welcome to the tip calculator")
x=float(input("What was the total bill? "))
y=int(input("How many people to split the bill? "))
z=int(input("What percentage tip would you like to give 10,12 or 15? "))

tip = x*(y/100)
pay= (x + tip)/y
print("Each person should pay")
print(pay)