
class Cash(object):    
    __cash_balance = 0

    def top_up(self, x): #u
        self.__cash_balance += x

    def count_1000(self): #c
        print(f"Количество тысяч: {self.__cash_balance // 1000}") 

    def take_away(self, x): #t
        if x >  self.__cash_balance:
            print("Недостаточно денег!")
            return
        self.__cash_balance -= x

comm = "-"
c = Cash()

while not comm == "q":
    
    while not comm in "qutc":
        comm = input("Введите команду (q, u, t, c)")
    
    if comm == "u":
       x = int(input("Введите сумму: "))
       c.top_up(x) 
    elif comm == "t":
        x = int(input("Введите сумму: "))
        c.take_away(x)
    elif comm == "c":
        c.count_1000()

    comm = "-"


