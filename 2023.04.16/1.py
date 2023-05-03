num1 = float(input('Первое число: '))
num2 = float(input('Второе число: '))
num3 = float(input('Третье число: '))

if num1 > 0 and num2 > 0 and num3 > 0:
    print(num1 + num2 + num3)
if num1 > 0 and num2 > 0 and num3 < 0:
    print(num1 + num2)
if num1 > 0 and num2 < 0 and num3 > 0:
    print(num1 + num3)    
if num1 < 0 and num2 > 0 and num3 > 0:
    print(num2 + num3)    
    
# Первое число: 2
# Второе число: -3
# Третье число: 2
# 4.0   

# Первое число: 3
# Второе число: 8
# Третье число: 10
# 21.0