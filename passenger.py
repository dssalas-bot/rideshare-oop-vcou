class PassAcc:
    def __init__(self, name, wallbalance):
        self.name = name
        self.__wallbalance = 0
        
       
       
    def top_up_wallet(self, amount):
        amount = int(input("Enter your desired amount: "))
        if amount < 0:
            print("Invalid amount!")
        else:
            print("{amount}"
            