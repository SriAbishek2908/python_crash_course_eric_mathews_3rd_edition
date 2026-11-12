# Using get() to Access Values

# alien_0 = {'color': 'green', 'speed': 'fast'}
# print(alien_0['points'])

alien_0 = {'color': 'green', 'speed': 'fast'}
point_value = alien_0.get('points', 'No points value assigned ')
print(point_value)