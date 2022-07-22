# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.


lst = [2,4,7,3,5,7,3,6,2]

def not_repeat_lst(lst):
    not_repeat = {i: lst.count(i) for i in lst}
    new_lst = [j for j in not_repeat.keys() if not_repeat[j] == 1]
    return new_lst
    
print(not_repeat_lst(lst))

# import random


# lenght = int(input('Введите длину массива '))
# lst = []
# high = int(input('верхняя граница '))
# low = int(input('нижняя граница '))
# for i in range(lenght):
#     lst.append(random.randint(0, 7))
# print(lst)