# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create 
# to 10. If you want to try more comparisons, write more tests and add them 
# to conditional_tests.py. Have at least one True and one False result for each of 
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method

# Test 1 : Equality and inequality with strings
name = 'sriabishek'
print(f"\nThe Name is : {name}")
if name == 'sriabishek':
    print("True")
    
name = 'sri'
if name != 'sriabishek':
    print("\nFalse")

# Test 2: Using the lower() method

name = 'SriAbishek'
if name.lower() == 'sriabishek':
    print("\nTrue")

# • Numerical tests involving equality and inequality, greater than and less 
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# Test 3: 
age_1 = 12
age_2 = 8
if age_1 <= 12 and age_2 <= 8:
    print("\nThe age 1 and 2 is True") 

age_3 = 28
age_4 = 56
if age_3 != 28 or age_4 == 56:
    print("\nThe Age 3 and 4 is True")
else:
    print("False")

# Test 4:  whether an item is in a list and whether an item is not in a list:

cars = ['audi','bmw','suzuki','toyota']
car = "audi"
if car in cars:
    print("\nTrue: The car name is in cars list")

banned_bikes = ['honda','enfield','triump','tvs']
usa_bikes = 'tvs'
if usa_bikes not in banned_bikes:
    print("Yes the bike is not in list")
else:
    print("The Bike is in the list")
    
