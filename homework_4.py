from random import randint
from time import sleep
from threading import Thread
import queue


class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args

    def guest_arrival(self, *args):
        guests = args
        for gue in guests:
            flag = True
            for tab in tables:
                if tab.guest is None:
                    tab.guest = gue
                    gue.start()
                    print(f'{gue.name} сел(-а) за стол номер {tab.number}')
                    flag = False
                    break
            if flag:
                self.queue.put(gue)
                print(f'{gue.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(tab.guest is not None for tab in tables):
            for tab in tables:
                if tab.guest is not None and not tab.guest.is_alive():
                    print(f'{tab.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {tab.number} свободен')
                    tab.guest = None
                    if not self.queue.empty():
                        tab.guest = self.queue.get()
                        print(f'{tab.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tab.number}>')
                        tab.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()