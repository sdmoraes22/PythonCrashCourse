people = ['mark', 'shawn', 'sara']

print(f"{people[0].title()} you are invited to dinner.")
print(f"{people[1].title()} you are invited to dinner.")
print(f"{people[2].title()} you are invited to dinner.")

print(f"{people[0].title()} can't go to dinner.")

people[0] = 'john'

print(f"{people[0].title()} you are invited to dinner.")
print(f"{people[1].title()} you are invited to dinner.")
print(f"{people[2].title()} you are invited to dinner.")