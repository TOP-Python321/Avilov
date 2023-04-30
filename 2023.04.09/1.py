name = input('Введите имя: ')
lastname = input('Введите фамилию: ')
age = int(input('Введите год рождения: '))
old = str(2023 - age)

# ИСПРАВИТЬ: согласно условию в данной задаче необходимо сформировать строку требуемого формата НЕ используя f-строку
print(f'{name + " " + lastname + ", " + old}')
# ИСПОЛЬЗОВАТЬ: ваш способ использования здесь f-строки неоптимален — вместо явной конкатенации строк намного эффективнее комбинировать символы в литерале строки с подставляемыми значениями:
#   f'{name} {lastname}, {old}'

# Авилов Александр, 33


# ИТОГ: доработать — 1/3
