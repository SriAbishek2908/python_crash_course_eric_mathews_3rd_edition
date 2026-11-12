# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a favorite 
# number for each person, and store each as a value in your dictionary. Print 
# each person’s name and their favorite number. For even more fun, poll a few 
# friends and get some actual data for your program.

favourite_numbers = {
    'abishek': 8,
    'sri': 12,
    'loser': 0,
    'lucifer': 8,
    'ravanan': 100,
    }

# print(f"Sri's favourite number is: {favourite_numbers['sri']}")
for name, num in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is: {num}")

# or alternate simple approach

# for name in favourite_numbers:
#     print(name, favourite_numbers[name])

