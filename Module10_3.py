import threading
import time
import random



class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 0
        while counter < 10:
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            s = random.randint(50,500)
            self.balance += s
            print(f'Пополнение {s}, баланс {self.balance}')
            time.sleep(0.01)
            counter +=1


    def take(self):
        counter = 0
        while counter < 10:
            s = random.randint(50,500)
            print(f'Запрос на {s}')
            if s > self.balance:
                self.lock.acquire()
                print(f'Запрос отклонен, недостаточно средств')
            if s <= self.balance:
                self.balance -= s
                print(f'Снятие {s} баланс {self.balance}')
            time.sleep(0.01)
            counter += 1







bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))



th1.start()
th2.start()

th1.join()
th2.join()



print(f'Итоговый баланс: {bk.balance}')