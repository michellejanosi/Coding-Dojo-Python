class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .02, initial_balance = 100):
        self.int_rate = int_rate
        self.__balance = initial_balance  # private so it can only be modified through the 'deposit' and 'withdrawal' methods
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited amount ${amount}. New balance: ${self.__balance}")
        else:
            print("The deposit amount must be greater than 0")
        return self

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.__balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.__balance}")
        return self

    def yield_interest(self):
        if self.__balance > 0:
            self.__balance += self.__balance * self.int_rate
        return self

    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(1250).deposit(2278).deposit(525).withdraw(1500).yield_interest().display_account_info()

account2.deposit(9082).deposit(1034).withdraw(2376).withdraw(1346).withdraw(145).withdraw(50).yield_interest().display_account_info()

BankAccount.display_all_accounts_info()
