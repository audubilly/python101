x = 2
y = 3

print('x = ', x)  # prints the value of x.

print('value of', x, '+', x, 'is', (x + x))  # prints the value of (x + x)

print('x = ')  # this is just a print statement

print((x + y), '= ', (y + x))  # prints the value of (x + y) and also (y + x).

radius = int(input('Enter radius: '))
pi = 3.14159

Diameter = 2 * radius
print(f'diameter is {Diameter}')

Circumference = 2 * pi * radius
print(f'Circumference is {Circumference}')

Area = pi * radius * radius
print(f'Area is {Area}')

rating = input('Enter an Integer  rating between 1 and 10')

# a = int(input('Enter an Integer  rating between 1 and 10'))
#
# print(rating + a)

# python does not collect other inputs via this method asides strings so it needs to be casted to an int.


# let x be the right operand

# let y be the right operand


x = 27.5
y = 2

print(27.5 + 2)

print(27.5 - 2)

print(27.5 * 2)

print(27.5 / 2)

print(27.5 // 2)

grade = 95

if grade >= 90:
    print('congratulations! your grade of', grade,
          ' has earned you an A in this Course')

amazon_cart = ['sunglasses', 'shoes', 'notebooks', 'clothes', 'bicycle', 'houses', 'video_games']
amazon_cart[3] = 'hoodies'
amazon_cart[2] = 'jackets'

amazon_cart.append('grapes')

amazon_cart.insert(3, 'boxers')

amazon_cart.extend(['jump', 'juice', 'jameson'])

print(amazon_cart)

# REMOVING ITEMS
amazon_cart.pop(3)
print(amazon_cart)

amazon_cart.pop(5)  # to pop off an item off a list via the INDEX.
print(amazon_cart)

amazon_cart.remove('jackets')  # to remove an item from a list .
print(amazon_cart)

user_name = input('Enter user_name: ')
password = input('Enter password: ')
hidden_password = '*' * len(password)

print(f'{user_name}, Your password, {hidden_password} ,is {len(password)} letters long')  # Password hider

is_old = False

if is_old:
    print('you can drive the car')
else:
    print('you are under aged')   # If conditional statement

is_friend = True

can_message = 'Message allowed' if is_friend else 'Message not allowed'  # Ternary operator
print(can_message)
