# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed 
# for the appropriate color alien.

alien_color = ['red','green','yellow']
for alien in alien_color:
    if alien == 'green':
        print(f"\nThe Alien color is: {alien}")
        print("The player has earned 5 points!")
    elif alien == 'yellow':
        print(f"\nThe Alien color is: {alien}")
        print("The player has earned 10 points!")
    else:
        print(f"\nThe Alien color is: {alien}")
        print("The Player has earned 15 points!")