# For Loop:
magicians = [ 'ramanan', 'ravanan', 'sita' ]
for magician in magicians:
    print(magician.title())

# Doing More Work Within a for Loop:
magicians = [ 'ramanan', 'ravanan', 'sita' ]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see the next trick, {magician.title()}.\n")

# Doing Something After a for Loop:
magicians = ['ramanan', 'ravanan', 'sita']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see the next trick, {magician.title()}.\n")

print(f"Thankyou everyone, That was a great magic show!")

# Forgetting to Indent:
# magicians = ['ramanan', 'ravanan', 'sita']
# for magician in magicians:
# print(magician)

# Forgetting to Indent Additional Lines:
# magicians = ['ramanan', 'ravanan', 'sita']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see the next trick, {magician.title()}.\n")

# Indenting Unnecessarily:
# magicians = ['ramanan', 'ravanan', 'sita']
#     print(magicians)

# Indenting Unnecessarily After the Loop:
# magicians = ['ramanan', 'ravanan', 'sita']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see the next trick, {magician.title()}.\n")
#     print("Thankyou everyone, That was a great magic show!")

# Forgetting the Colon:
# magicians = ['ramanan', 'ravanan', 'sita']
# for magician in magicians
#     print(magician)