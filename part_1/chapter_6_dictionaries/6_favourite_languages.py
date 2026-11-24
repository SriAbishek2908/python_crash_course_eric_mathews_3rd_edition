
favourite_languages = {
    'lucifer' : 'java',
    'sri': 'c++',
    'abishek': 'python',
    'loser': 'python',
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

# ---------------------------------------------------------------------------------

# Looping Through All the Keys in a Dictionary

favourite_languages = {
    'lucifer' : 'java',
    'sri': 'c++',
    'abishek': 'python',
    'loser': 'python',
}

for name in favourite_languages.keys():
    print(name.title())

# ---------------------------------------------------------------------------------

favourite_languages = {
    'lucifer' : 'java',
    'sri': 'c++',
    'abishek': 'python',
    'loser': 'python',
}

friends = ['sri', 'loser']
for name in favourite_languages.keys():
    print(f"\n{name.title()}")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\n\t{name.title()}, I see, you love {language.title()} ")

# ------------------------------------------------------------------------------

# Looping Through a Dictionary’s Keys in a Particular Order

favourite_languages = {
    'lucifer' : 'java',
    'sri': 'c++',
    'abishek': 'python',
    'loser': 'python',
}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, Thankyou for taking the POll!")