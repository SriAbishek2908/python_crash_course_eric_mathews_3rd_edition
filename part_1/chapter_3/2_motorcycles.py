motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[1] = 'tvs'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1,'hero')
print(motorcycles)

message = f"My favourite motorcycle is {motorcycles[2].title()}"
print(message)

motorcycles.insert(2,'kawasaki')
message_1 = motorcycles[2]
print(f"My favourite motorcycle is {message_1}")
print(motorcycles)

#Removing an item from a list using the del statement

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#Removing an item from a list using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

#Using Strings with Pop() method 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f"The Last Motorcycles I Owned was {last_owned.title()}.")

#Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The First Motorcycle that I Owned was {first_owned.title()}.")