num = int(input('Введите число: '))

# ДОБАВИТЬ: в ситуациях, когда речь не идёт о больших объёмах данных, лучше не выполнять несколько раз одинаковые вычисления, а вычислив однажды, сохранить результат в переменные и использовать их в дальнейшем

print(f'Сумма цифр = {(num // 100) + (num // 10 % 10) + (num % 10)}\n'
      f'Произведение цифр = {(num // 100) * (num // 10 % 10) * (num % 10)}')

# Сумма цифр = 12
# Произведение цифр = 28


# ИТОГ: хорошо — 3/4
