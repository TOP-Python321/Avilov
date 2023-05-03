num1 = input()
num2 = input()

box1 = (ord(num1[0]) + int(num1[1])) % 2
box2 = (ord(num2[0]) + int(num2[1])) % 2

if box1 == box2:
    print('Да')
else:
    print('Нет')
    
# a2
# a4
# Да

# a1
# a2
# Нет    