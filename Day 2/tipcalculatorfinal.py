print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give?"))
no_of_people=int(input("How many people to split the bill"))
pay=((bill*tip/100)+bill)/no_of_people
pay=round(pay,2)
pay="{:.2f}".format(pay)
print(f"Each person should pay ${pay}")