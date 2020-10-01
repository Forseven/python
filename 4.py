# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


user_number = input("ВВедите положительное целое число: ")

number = 0
max = 0
while number < len(user_number):

    if max < int(user_number[number]):
        max = int(user_number[number])

    number +=1
print("max number:  %s" %  str(max))