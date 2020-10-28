from random import randint




class Card:

    data = None

    def __init__(self):
        uniques = []
        while len(uniques) < 90:
            new = randint(1, 90)
            if new not in uniques:
                uniques.append(new)

        self.data = []
        for i in range(0, 3):
            tmp = sorted(uniques[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = randint(0, len(tmp))
                tmp.insert(index, 0)
            self.data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        string = delimiter + '\n'
        for index, num in enumerate(self.data):
            if num == 0:
                string += '  '
            elif num == -1:
                string += ' X'
            else:
                string += str(num)

            if (index + 1) % 9 == 0:
                string += '\n'
            else:
                string += ' '

        return string + delimiter

    def __contains__(self, item):
        return item in self.data

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = -1
                return
        raise ValueError(f' Нет на карточке: {num}')

    def closed(self) -> bool:
        return set(self.data) == {0, -1}

class Game:

    def __init__(self):
        self.usercard = Card()
        self.compcard = Card()
        self.kegs = []
        while len(self.kegs) < 90:
            new = randint(1, 90)
            if new not in self.kegs:
                self.kegs.append(new)


    def start (self):
        keg = self.kegs.pop() # Remove and return item at index (default last).
        print(f'Новый бочонок: {keg} (осталось {len(self.kegs)})')
        print(f'       Игрок     \n{self.usercard}')
        print(f'     Компьетер   \n{self.compcard}')

        answer = input('Зачеркнуть цифру? (y/n) ').lower().strip()

        if answer == 'y' and not keg in self.usercard or answer != 'y' and keg in self.usercard:
            return 2

        if keg in self.usercard:
            self.usercard.cross_num(keg)
            if self.usercard.closed():
                return 1
        if keg in self.compcard:
            self.compcard.cross_num(keg)
            if self.compcard.closed():
                return 2

        return 0

game = Game()
while True:
    result = game.start()
    if result == 1:
        print('ПОбеда')
        break
    elif result == 2:
        print('проиграл')
        break

