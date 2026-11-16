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

