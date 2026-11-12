# If-elif-else Chain :
age = 16
print(f"Your Age:{age}")
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# Alternate concise method :

age = 22
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"Your Age:{age}")
print(f"Your admission price is :${price}")

# Multiple If-elif-else block:

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <= 65:
    price = 40
else:
    price = 20

print(f"Your Age:{age}")
print(f"Your admission cost is : ${price}")

# Omitting else block :

age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your Age:{age}")
print(f"Your admission cost is : ${price}")