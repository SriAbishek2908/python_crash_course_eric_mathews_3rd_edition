# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of 
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the 
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in 
# your list.

guests = ['Duraiyammal', 'Chinnammal', 'Muthuvel']
unable_to_attend = guests.pop()
print(f"Dear {unable_to_attend}", "It's unfornunate that you can't make it to the dinner. I will miss your presence and hope to catch up with you soon.")

guests.append('Hitler') 
print(guests)
new_guest = guests[-1]
print(f"Dear {new_guest}, I would like to invite you to dinner. I would be delighted if you could join me for an evening of great food and conversation. Looking forward to your presence!")
