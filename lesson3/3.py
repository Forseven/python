# Task 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(arg1, arg2, arg3):
    numbers = [arg1, arg2, arg3]
    numbers.sort()
    return numbers[1] + numbers[2]


print(my_func(12.43, 56.4, 32))
