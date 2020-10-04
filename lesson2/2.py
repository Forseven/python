# Task 2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

my_list = []
cl = int(input("Введите количество элементов списка: "))
number = 0
while number < cl:
    my_list.append(input("Введите значение списка № %s: " % (number+1)))

    number += 1

number = 0
l = len(my_list)
if len(my_list) % 2 > 0:
    l = (len(my_list)) - 1

while number < l:
    a = my_list[number+1]
    my_list[number+1] = my_list[number]
    my_list[number] = a
    number += 2


print(my_list)