# Using the range() function: 
for value in range(1, 6):
    print(value)

# Using range() to make a list of numbers:
numbers = list(range(1,6))
print(numbers)

# Using range() to make a list of even or odd numbers:
numbers = list(range(1,31))
print(f"The original sequence numbers list: {numbers}")
even_numbers = list(range(2,21,2))
print(f"The Even Numbers List: {even_numbers}")
odd_numbers = list(range(1,22,2))
print(f"The Odd Numbers List: {odd_numbers}")

# Using range to create Set of numbers:
squares = []
for value in range (1,11):
    squares.append(value**2)
print(f"The Squares List: {squares}")

# Simple Statistics with a List of Numbers::
digits = [1,2,3,4,5,6,7,8,9,10]
print(f"The Minimum Value in the List: {min(digits)}")
print(f"The Maximum Value in the List: {max(digits)}")
print(f"The Sum of the digits in the List: {sum(digits)}")
