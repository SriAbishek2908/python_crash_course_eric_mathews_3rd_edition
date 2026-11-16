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



# List Comprehensions:
squares = [value**2 for value in range(1,11)]
print(squares)