my_foods = ['pizza', 'falafel', 'carrot_cake']
friend_foods = my_foods[:]

# if it's used that way will show the wrong result
# friend_foods = my_foods

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)