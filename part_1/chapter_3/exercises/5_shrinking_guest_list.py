# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print a 
# message to that person letting them know you’re sorry you can’t invite them 
# to dinner.
# • Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end of 
# your program

guests = ['Gandhi', 'Duraiyammal', 'Nehru', 'Chinnammal', 'Muthuvel', 'Ambedkar']
print(f"{guests}Apologies! I can invite only two people for dinner.")


shrink_guests = guests.pop(0)
print(f"Dear Gandhi, I am sorry I can't invite you to dinner.")
shrink_guests = guests.pop(1)
print(f"Dear Nehru, I am sorry I can't invite you to dinner.")
shrink_guests = guests.pop(1)
print(f"Dear Chinnammal, I am sorry I can't invite you to dinner.")
shrink_guests = guests.pop(1)
print(f"Dear Muthuvel, I am sorry I can't invite you to dinner.")

print(f"Dear {guests[0]} , {guests[-1]} you are still invited to dinner.")

del guests[0]
del guests[0]
print(guests)