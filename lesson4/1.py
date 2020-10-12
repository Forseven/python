import argparse
# Task 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


def my_func(hours, rate, premium):
    return (hours * rate) + premium


parser = argparse.ArgumentParser(description='Script')
parser.add_argument('-v', action="store", dest="hours", default=0, type=int, help='выработка в часах')
parser.add_argument('-r', action="store", dest="rate", default=0, type=int, help='ставка в час')
parser.add_argument('-p', action="store", dest="premium", default=0, type=int, help='премия')
args = parser.parse_args()

if __name__ == '__main__':
    print(f'Salary: {my_func(args.hours, args.rate, args.premium)}')



#usage: 1.py [-h] [-v HOURS] [-r RATE] [-p PREMIUM]
#Script
#optional arguments:
#  -h, --help  show this help message and exit
#  -v HOURS    выработка в часах
#  -r RATE     ставка в час
#  -p PREMIUM  премия
