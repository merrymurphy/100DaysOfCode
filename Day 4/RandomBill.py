# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x=len(names)
# print(x)
index=random.randint(0,x-1)
# print(index)

bill=names[index]
print(f"{bill} is going to buy the meal today")

# print(random.choice(names))
