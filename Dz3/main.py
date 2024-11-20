class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} грн добавлено. Баланс: {self.balance} грн")
        else:
            print("Сумма має бути більше за 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} грн снято. Баланс: {self.balance} грн")
        else:
            print("Недостатньо коштів або неправильна сумма")

    def show_info(self):
        print(f"{self.owner}, рахунок {self.account_number}: {self.balance} грн")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(owner, account_number, initial_balance)
            print(f"Рахунок {account_number} створенно для {owner}")
        else:
            print("Рахунок з таким номером вже існує")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Рахунок не знайдено")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Рахунок не знайдено")

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.accounts.get(from_acc)
        to_account = self.accounts.get(to_acc)
        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Переказано {amount} грн з {from_acc} на {to_acc}")
            else:
                print("Недостатньо коштів для переказу")
        else:
            print("Один із рахунків не знайденно")

    def show_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.show_info()
        else:
            print("Рахунок не знайденно")


# Приклад використання
bank = Bank()
bank.create_account("Іван Іванов", "123", 1000)
bank.create_account("Олена Петрова", "456", 500)

bank.deposit("123", 200)
bank.withdraw("456", 100)
bank.transfer("123", "456", 300)

bank.show_account("123")
bank.show_account("456")
