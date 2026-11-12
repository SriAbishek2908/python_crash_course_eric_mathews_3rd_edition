# Try these short programs to get some firsthand experience with Python’s lists. 
# You might want to create a new folder for each chapter’s exercises, to keep 
# them organized.
# ----------------------------------------------------------------------------------------
# 3-1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.

names = ['Sri', 'Abi', 'Loser', 'Lucifer']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# ----------------------------------------------------------------------------------------
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each mes
# sage should be the same, but each message should be personalized with the 
# person’s name.

message_1 = f"Hello {names[0]}! You are a failure"
message_2 = f"Hello {names[1]}! You are a failure"
message_3 = f"Hello {names[2]}! You are a failure"
message_4 = f"Hello {names[3]}! You are a failure"
print(f"{message_1}\n{message_2}\n{message_3}\n{message_4}")

# ---------------------------------------------------------------------------------------

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.

favourite_transport = ['car', 'bike', 'bus', 'train', 'motorcycle']
message = f"I would like to own a Honda {favourite_transport[0]}"
message_1 = f"I would like to own a Yamaha {favourite_transport[1]}"
message_2 = f"I would like to own a Volvo {favourite_transport[2]}"
message_3 = f"I would like to own a Shatabdi {favourite_transport[3]}"
message_4 = f"I Would like to own a Harley Davidson {favourite_transport[4]}"
print(f"{message}\n{message_1}\n{message_2}\n{message_3}\n{message_4}")