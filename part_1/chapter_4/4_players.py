# Slicing a List:

players = ['Virat', 'Rohit', 'MSD', 'Jadeja', 'Raina', 'Yuvaraj', 'Bumrah', 'Shami', 'Ashwin', 'Rahul']
print(players[2:4])
print(players[:4])
print(players[0:])
print(players[-7:])

print(f"List of every odd players: {players[0::2]}")

# Looping Through a Slice:

players = ['Virat', 'Rohit', 'MSD', 'Jadeja', 'Raina', 'Yuvaraj', 'Bumrah', 'Shami', 'Ashwin', 'Rahul']
print("The legendary 5 players in my list are: ")
for player in players[:6]:
    print(player.title())