# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a 
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to 
# print the last three items in the list.
# -----------------------------------------------------------------------------------
cricaholics = ['Kailash', 'cyril', 'mauriya', 'simeon', 'abishek', 'sunil', 'sparks', 'ajay', 'ak', 'lokesh', 'lelith']
print(f"The Playing squad is : {cricaholics}")

print(f"The first three players in the list: {cricaholics[:3]}")
print(f"The Three player in the middle of the list: {cricaholics[3:8]}")
print(f"The last three players in the list: {cricaholics[7:]}")

# ------------------------------------------------------------------------------------
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).  
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the 
# following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite piz
# zas are:, and then use a for loop to print the first list. Print the message My 
# friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
# -------------------------------------------------------------------------------------

my_pizzas = ['Margherita', 'Farmhouse', 'Peppy Paneer', 'Veggie Paradise', 'Mexican Green Wave']
firends_pizzas = my_pizzas[:]
print(f"My Favorite Pizzas are: {my_pizzas}")
print(f"My Friends Favorite Pizzas are: {firends_pizzas}")
my_pizzas.append('Chicken Tikka')
firends_pizzas.append('Chicken Dominator')
print("My Favorite Pizzas are: ")
for pizza in my_pizzas:
    print(pizza.title())
print("My Friends Favorite Pizzas are: ")
for pizza in firends_pizzas:
    print(pizza.title())


# -------------------------------------------------------------------------------------
# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing, to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.

my_foods = ['Parotta', 'Biryani', 'Meals', 'Dosa', 'Idli']
friend_foods = my_foods[:]

print("My Favorite Foods are: ")
for food in my_foods:
    print(food.title())

print("My friends Favorite Foods are: ") 
for food in friend_foods:
    print(food.title())
    
   