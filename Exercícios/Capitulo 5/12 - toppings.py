# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print(f"Sorry we are out of {requested_topping} right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
# else:
#     print("Are you sure you want a plain pizza?")

avaiable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}.")

print("\nFinished making your pizza!")