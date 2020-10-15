# task 1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
file_handler = open("1.txt","w",encoding="utf8")

while True:
    text = input("Enter text, blank string to exit: ")
    if  text == "":
        file_handler.close()
        break
    file_handler.write('%s \n' % text)


