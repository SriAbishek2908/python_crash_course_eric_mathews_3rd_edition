# Checking whether the value is not in a list:

banned_users = ['carolina', 'andrew','david']
users = ['sri','abi','lucifer','loser','andrew']
for user in users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response if you wish!")
    else:
        print(f"{user.title()}, You are Banned to post a response")