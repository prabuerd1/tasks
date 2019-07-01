class Vending_Machine:

    def __init__(self):
        print("Welcome To Megam Cool drings")
        self.balance_cash = 0
        self.bill_value = 0

    def cash_details(self):
        self.cash = int(input("Enter your cash "))
        print("Your cash value is ", self.cash)
        return 0

    def stock_deatils(self):
        self.stock = [20, 20, 20, 20]
        self.price = [20, 22, 30, 35]
        self.brand = ["Fruity","Bovanto","Mazza","slice"]
        return 0

    def product_deatils(self):
        print("Please chose your product based on No(1 to 4)  \n 1.Fruity Rs.20 \n 2.Bovanto Rs.22 \n 3.Mazza Rs.30 \n 4.slice Rs.35")
        self.product = int(input("Enter produt No"))
        self.qty = int(input("Enter Quantity "))

        if (self.product == 1):
            self.bill_value = self.qty * self.price[0]
            self.stock[0] = self.stock[0] - self.qty
            self.balance_cash = self.cash - self.bill_value
            print("Your purchased prouct is",self.brand[0])
            print("You bill value is",self.bill_value)
            print("Your balanced cash is",self.balance_cash)

        elif (self.product == 2):
            self.bill_value = self.qty * self.price[1]
            self.stock[1] = self.stock[1] - self.qty
            self.balance_cash = self.cash - self.bill_value
            print("Your purchased prouct is",self.brand[1])
            print("You bill value is",self.bill_value)
            print("Your balanced cash is",self.balance_cash)

        elif (self.product == 3):
            self.bill_value = self.qty * self.price[2]
            self.stock[2] = self.stock[2] - self.qty
            self.balance_cash = self.cash - self.bill_value
            print("Your purchased prouct is",self.brand[2])
            print("You bill value is",self.bill_value)
            print("Your balanced cash is",self.balance_cash)

        elif (self.product == 4):
            self.bill_value = self.qty * self.price[3]
            self.stock[3] = self.stock[3] - self.qty
            self.balance_cash = self.cash - self.bill_value
            print("Your purchased prouct is",self.brand[3])
            print("You bill value is",self.bill_value)
            print("Your balanced cash is",self.balance_cash)
        else:
            print("you entered wrong input")

        return 0

    def current_stock(self):
        print("Current Stock status is")
        print(self.brand[0],self.stock[0])
        print(self.brand[1],self.stock[1])
        print(self.brand[2],self.stock[2])
        print(self.brand[3],self.stock[3])
        return 0

vm = Vending_Machine()
vm.cash_details()
vm.stock_deatils()
vm.product_deatils()
vm.current_stock()










#self.rs_50 = input("Enter no of 50's ")
#self.rs_10 = input("Enter no of 10's ")
#self.rs_1 = input("Enter no of 10's ")
#self.total_cash = (int(self.rs_100) * 100) + (int(self.rs_50)
                  # * 50) + (int(self.rs_10) * 10) + (int(self.rs_1) * 1)
