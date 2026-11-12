alien_0 = {'x_position': 0 , 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be fast alien:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

# Changing speed :
alien_0 = {'x_position': 0 , 'y_position': 25, 'speed': 'fast'}
# alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be fast alien:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"\nNew x_position: {alien_0['x_position']}")

