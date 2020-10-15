# Task 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random


my_file = open("5.txt", "w", encoding="utf8")


for i in range(10):
    my_list = random.sample(range(10, 100), 10)
    my_file.write("%s\n" % (' '.join(map(str, my_list))))
my_file.close()
file_handler = open("5.txt")
lines = file_handler.readlines()
all_sum = 0
for i, line in enumerate(lines):
    line_sum = sum([int(el) for el in line.split(" ")])
    all_sum += line_sum
    print(f'Строка № {i +1} , сумма {line_sum}')

print(f'Сумма всех чисел в файле {all_sum}')