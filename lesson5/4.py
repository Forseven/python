# Task 4
# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_f = open("4.txt")
my_new_file = open("4_new.txt", "w",encoding="utf8")
my_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
for line in my_f:
    new_line = f''
    print(line.replace(line.split(" ")[0],my_dict[int(line.split(" ")[2].strip())]))
    my_new_file.write(line.replace(line.split(" ")[0],my_dict[int(line.split(" ")[2].strip())]))
my_new_file.close()
my_f.close()