# Looping Through All Key-Value Pairs
user = {'username':'SriAbishek',
        'first': 'sri',
        'last':'abishek'}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value.title()}")
