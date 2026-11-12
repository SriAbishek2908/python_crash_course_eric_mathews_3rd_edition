# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test. Your code 
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line 
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another 
# 5 tests evaluate to False

# Test 1:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

# Test 2:
age = 19
print("\nIs age == 19? I predict True.")
print(age == 19)

print("Is age >= 21? I predict False.")
print(age == 21)

# Test 3:
name = 'abi'
print("\nIs name == 'abi'? I predict True")
print(name=='abi')

print("Is name == 'sri'? I predict False")
print(name=='sri')

# Test 4:
pizza_toppin = 'mushroom'
print("\nIs pizza_toppin == 'mushroom'? I predict True")
print(pizza_toppin=='mushroom')

print("Is pizza_toppin == 'pineapple'? I predict False")
print(pizza_toppin=='pineapple')

# Test 5:
mark = 98
print("\nIs mark == 98 ? I predict True")
print(mark==98)

print("Is mark == 95 ? I predict False")
print(mark==95)

# ---------------------------------------------------------------------------------------------------

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre
# ate to 10. If you want to try more comparisons, write more tests and add them 
# to conditional_tests.py. Have at least one True and one False result for each of 
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less 
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# Tests for equality and inequality with strings:
name = 'sriabishek'
print(f"\n{name}")
if name == 'sriabishek':
    print("The name is True")
name = 'abi'
print(f"\n{name}")
if name != 'sri':
    print("The name is False")

