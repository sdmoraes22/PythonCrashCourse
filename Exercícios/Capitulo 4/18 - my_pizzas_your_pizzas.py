my_pizzas = ['mussarella', 'peperonni', 'catupiry']
friend_pizzas = my_pizzas[:]

my_pizzas.append('portuguese')
friend_pizzas.append('chocolate')

for pizza in my_pizzas:
    print(f"My favorite pizzas are {pizza}")

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are {pizza}")