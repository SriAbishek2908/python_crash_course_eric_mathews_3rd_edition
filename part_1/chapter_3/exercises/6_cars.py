# 3-8. Seeing the World: Think of at least five places in the world you’d like  
# to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; 
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without chang
# ing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its 
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show 
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order. 
# Print the list to show that its order has changed.


places = ['australia', 'new-zeland', 'jappan', 'usa', 'faroe-islands']
print(places)

print(sorted(places))
print(f"Original list: {places}")
places.reverse()
print(f"Reversed list: {places}")
places.reverse()
print(f"Original list: {places}')")
places.sort()
print(f"Sorted List: {places}')")
places.sort(reverse=True)
print(f"Reverse Sorted List: {places}')")

# --------------------------------------------------------------------------------------------------------------
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (pages 41–42), use len() to print a message indicating the number 
# of people you’re inviting to dinner.


guests = ['Duraiyammal', 'Chinnammal', 'Muthuvel']
print(f"The Lengith of the Guests for dinner is : {len(guests)}")

# -------------------------------------------------------------------------------------------------------------
# 3-10. Every Function: Think of things you could store in a list. For example, you 
# could make a list of mountains, rivers, countries, cities, languages, or anything 
# else you’d like. Write a program that creates a list containing these items and 
# then uses each function introduced in this chapter at least once.

my_list = ['hyundai', 'sabarimala', 'new-zeland', 'python', 'loser']
my_list.sort()
print(f"Sort Method used list: {my_list}")

my_list.sort(reverse=True)
print(f"Reverse Sort Method Used List: {my_list}")

print(f"Original List: {my_list}")
print("Sorted Function Used List : {sorted(my_list)}")

my_list.reverse()
print(f"Reversed List: {my_list}")

my_list.reverse()
print(f"Original List: {my_list}")

print(f"Length of the Original List: {len(my_list)}")


