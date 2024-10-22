# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

print('Введите первое число:')
first = int(input())
print('Введите второе число:')
second = int(input())
print('Введите третье число:')
third = int(input())

if first == second and first == third:
    print('Вы ввели 3 одинаковых числа: ', first)
elif first == second or first == third or second == third:
    if first == second:
        print('Вы ввели 2 одинаковых числа: ', first)
    elif first == third:
        print('Вы ввели 2 одинаковых числа: ', first)
    else:
        print('Вы ввели 2 одинаковых числа: ', second)
else:
    print('Введены разные числа')