# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import datetime

seconds = int(input("Введите количество секунд "))
print(print("Время в формате чч:мм:сс  , %s!" % str(datetime.timedelta(seconds=seconds))))
