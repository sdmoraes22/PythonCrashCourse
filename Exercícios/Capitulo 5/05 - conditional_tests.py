car = 'subaru'

print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

car = 'BMW'
print("\nIs car == 'BMW'? I predict True")
print(car == 'BMW')

car = 'Nissan'
print("\nIs car == 'Nissan'? I predict True")
print(car == 'Nissan')

car = 'Subaru'
print("\nIs car == 'audi'? I predict True")
print(car == 'Subaru')

car = 'Ford'
print("\nIs car == 'audi'? I predict True")
print(car == 'Ford')

car = 'Acura'
print("\nIs car == 'audi'? I predict True")
print(car == 'Acura')


car = 'BMW'
print("\nIs car == 'BMW'? I predict False")
print(car == 'bmw')

car = 'Nissan'
print("\nIs car == 'Nissan'? I predict False")
print(car == 'nissan')

car = 'Subaru'
print("\nIs car == 'audi'? I predict False")
print(car == 'subaru')

car = 'Ford'
print("\nIs car == 'audi'? I predict False")
print(car == 'ford')

car = 'Acura'
print("\nIs car == 'audi'? I predict False")
print(car == 'acura')


car = 'Acura'
print("\nIs car == 'audi'? I predict True")
print(car.lower() == 'acura')

car = 'Acura'
print("\nIs car == 'audi'? I predict False")
print(car.lower() == 'bmw')

number = 11
print(f"\nIs number {number} > 10? I predict True")
print(number > 10)

number = 11
print(f"\nIs number {number} < 10? I predict False")
print(number < 10)


number = 11
print(f"\nIs number {number} < 10 or {number} > 10? I predict True")
print(number < 10 or number > 10)


number = 11
print(f"\nIs number {number} < 10 or {number} > 11? I predict False")
print(number < 10 or number > 11)



number = 11
print(f"\nIs number {number} > 10 and {number} < 12? I predict True")
print(number < 10 or number > 11)

number = 11
print(f"\nIs number {number} > 10 and {number} > 12? I predict False")
print(number < 10 or number > 12)

cars = ['subaru', 'bmw', 'ford']
print(f"\nIs 'subaru' in cars? I predict True")
print('subaru' in cars)

print(f"\nIs 'lamborghini' in cars? I predict False")
print('lamborghini' in cars)

print(f"\nIs 'lamborghini' not in cars? I predict True")
print('lamborghini' not in cars)

