# TRY IT YOURSELF
# Save each of the following exercises as a separate file, with a name like name 
# _cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

#----------------------------------------------------------------------

# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”

name = "Sri Abishek"
message = (f"Hello {name}! would you like to learn some python today ?")
print(message)

#--------------------------------------------------------------------------------
# 2-4. Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

name = "Sri Abishek"
print(name.upper())
print(name.lower())
print(name.title())

#---------------------------------------------------------------------------------

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never 
# tried anything new.”

name = "Sri Abishek"
quote = "I had an epiphany : I was a Loser"
message = (f'{name} once said, {quote}')
print(message)

#------------------------------------------------------------------------------
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
# person’s name using a variable called famous_person. Then compose your mes
# sage and represent it with a new variable called message. Print your message.

famous_person = "Sri Abishek"
message  = f"{famous_person} once said, I had an epiphany : I was a loser"
print(message)

#------------------------------------------------------------------------------
# 2-7. Stripping Names: Use a variable to represent a person’s name, and 
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().

name = " \nSri Abishek\t "
print(name.lstrip())
print(name.rstrip())
print(name.strip())


#------------------------------------------------------------------------------
# 2-8. File Extensions: Python has a removesuffix() method that works exactly  
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
# filename. Then use the removesuffix() method to display the filename without 
# the file extension, like some file browsers do.

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# ------------------------------------------------------------------------------

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should be four lines, with the number 8 appearing once on 
# each line.

print(6+2)
print(10-2)
print(2*4)
print(64/8)

# -------------------------------------------------------------------------------


# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, 
# using that variable, create a message that reveals your favorite number. Print 
# that message

favourite_numbers = 8
message = (f"My favourite number is {favourite_numbers}")
print(message)

# ------------------------------------------------------------------------------

# 2-12. Zen of Python: Enter import this into a Python terminal session and skim 
# through the additional principles

import this 