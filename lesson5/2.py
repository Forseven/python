# Task 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file_handler =  open("2.txt")

lines = file_handler.readlines()
print(f'String count: {len(lines)}')

for i,line in enumerate(lines):
    print(f'Срока № {i+1}, Количество слов: {len(line.split(" "))}')