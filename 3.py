# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input("ВВедите положительное целое число: "))
number = 1
total = 0
n = ""
while number <= user_number:
    n = n + str(user_number)
    total = int(n)+total
    print(n)
    number = number+1

print(total)
