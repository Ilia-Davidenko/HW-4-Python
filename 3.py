# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


number = int(input('Введите натуральное число '))

def multipliers(number: list):
    lst_num = []
    count = 2
    while (number / count) > 1:
        if number % count == 0:
            lst_num.append(count)
            number /= count
        count += 1
    return lst_num

print(multipliers(number))