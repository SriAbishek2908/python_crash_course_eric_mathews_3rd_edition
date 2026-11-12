# Using If Statements With Lists:

requested_toppings = ['mushrooms','green peppers','pineapple','extra cheese']
for toppings in requested_toppings:
    print(f"Adding {toppings}")

print("\nFinished making your pizza!")

# Checking If Statements:

requested_toppings = ['mushrooms','green peppers','pineapple','extra cheese']
print("\nChecking If Statements with Lists:")
for toppings in requested_toppings:
    if toppings == 'green peppers': 
        print("Sorry, We are out of green peppers now.")
    else:
        print(f"Adding {toppings}")

print("\nFinished making your Pizza.")

# ------------------------------------------------------------------------------

# Checking That a List is Not Empty:
print("\nChecking That a List is Not Empty:")
requested_toppings = []
if requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}")
        print("\nFinished making your pizza!")
else:
    print("Are your sure you want plain pizza?")

# Using Multiple Lists:
print("\nUsing Multiple Lists:")

available_toppings = ['mushrooms','pepperoni','olives','green peppers','pineapples','extra cheese']

customer_requested_toppings = ['mushrooms','french fries','extra cheese']

for toppings in customer_requested_toppings:

    if toppings in available_toppings:
        print(f"Adding {toppings}")
    else:
        print(f"Sorry we don't have {toppings} as toppings.")

print("Finished making your pizza!")