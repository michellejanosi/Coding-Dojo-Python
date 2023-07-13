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


class User:
    all_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Dictionary to store the different types of bank accounts
        User.all_users.append(self)

    def add_account(self, type_of_account, int_rate, initial_balance = 0):
        # Create a new bank account and add it to the accounts dictionary
        self.accounts[type_of_account] = BankAccount(int_rate, initial_balance)
        return self

    def make_deposit(self, type_of_account, amount):
        if type_of_account in self.accounts:
            self.accounts[type_of_account].deposit(amount)
        else:
            print(f"No {type_of_account} exists for {self.name}.")
        return self

    def make_withdrawal(self, type_of_account, amount):
        if type_of_account in self.accounts:
            self.accounts[type_of_account].withdraw(amount)
        else:
            print(f"No {type_of_account} exists for {self.name}.")
        return self

    def display_user_balance(self, type_of_account):
        if type_of_account in self.accounts:
            self.accounts[type_of_account].display_account_info()
        else:
            print(f"No {type_of_account} exists for {self.name}.")
        return self


    def transfer_money(self, type_of_account, amount, other_user):
        if type_of_account in self.accounts and type_of_account in other_user.accounts:
            if self.accounts[type_of_account].withdraw(amount):
                other_user.accounts[type_of_account].deposit(amount)
                print(f"Transferred ${amount} from {self.name}'s {type_of_account} to {other_user.name}'s {type_of_account}")
            else:
                print(f"Insufficient funds in {self.name}'s {type_of_account}")
        else:
            print(f"No {type_of_account} account exists for either {self.name} or {other_user.name}")
        return self

    @classmethod
    def display_all_accounts_info(cls):
        for user in cls.all_users:
            print(f"User: {user.name}, Email: {user.email}")
            for account_type, account in user.accounts.items():
                print(f"Account Type: {account_type}")
                account.display_account_info()


user1 = User("Alice", "alice@gmail.com")
user1.add_account("Checking", 0.01, 500)
user1.add_account("Savings", 0.02, 1000)

user2 = User("Bob", "bob@gmail.com")
user2.add_account("Checking", 0.01, 700)
user2.add_account("Savings", 0.02, 1500)

user1.make_deposit("Checking", 500).make_withdrawal("Savings", 200).display_user_balance("Checking").display_user_balance("Savings")

user2.make_deposit("Saving", 500).make_withdrawal("Checking", 200).display_user_balance("Checking").display_user_balance("Savings")

# Transferring money from Alice's checking account to Bob's saving account
user1.transfer_money("Checking", 200, user2)
user1.display_user_balance("Checking")
user2.display_user_balance("Savings")

User.display_all_accounts_info()
