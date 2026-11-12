# A Simple Dictionary:
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_color = alien_0['color']
new_points = alien_0['points']
print(f"The Alien color you just shot down is : {alien_color.title()}")
print(f"You have earned {new_points} points!")


# Adding New Key Value Pairs:
alien_0['x_positions'] = 0
alien_0['y_positions'] = 25
print(f"After adding new key value pairs :\n {alien_0}")

# Starting with an empty dictionary:
alien_00 = {}
alien_00['color'] = 'black'
alien_00['points'] = 100
print(f"The Empty Dictionary after adding values are :\n{alien_00}")

# Modifying Values in a Dictionary:
alien_000 = {'color':'green'}
print(f"The alien is {alien_000['color']}")

alien_000['color'] = 'black'
print(f"The alien is now {alien_000['color']}")

