people = ['mark', 'shawn', 'sara']
people.insert(0, 'john')
people.insert(3, 'michelle')
people.append('josh')

uninvited_people = people.pop()

print(f"Sorry {uninvited_people.title()} i don't have anymore places for the dinner")
uninvited_people = people.pop()
print(f"Sorry {uninvited_people.title()} i don't have anymore places for the dinner")
uninvited_people = people.pop()
print(f"Sorry {uninvited_people.title()} i don't have anymore places for the dinner")
uninvited_people = people.pop()
print(f"Sorry {uninvited_people.title()} i don't have anymore places for the dinner")

print(f"{people[0].title()} you are invited to dinner.")
print(f"{people[1].title()} you are invited to dinner.")

del people[1]
del people[0]

print(people)