class BankAccount:

    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def print_balance(self):
        print("Your current balance is:")
        print(self.balance)

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Please enter a valid amount.")

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("You don't have enough funds to make this withdrawal.")


class SavingsBankAccount(BankAccount):
    INTEREST_RATE = 0.035

    def __init__(self, owner, balance, currency):
        BankAccount.__init__(self, owner, balance, currency)
        self.interest_rate = SavingsBankAccount.INTEREST_RATE

    def deposit_interest_earned(self):
        interest_earned = self.balance * SavingsBankAccount.INTEREST_RATE
        self.balance += interest_earned


class CheckingBankAccount(BankAccount):

    def __init__(self, owner, balance, currency, debit_card=None, credit_card=None):
        BankAccount.__init__(self, owner, balance, currency)
        self.debit_card = debit_card
        self.credit_card = credit_card


my_savings_account = SavingsBankAccount("Nora Nav", 45600, "USD")

my_savings_account.print_balance()
my_savings_account.make_deposit(5000)
my_savings_account.make_withdrawal(200)

my_savings_account.deposit_interest_earned()
my_savings_account.print_balance()

my_checking_account = CheckingBankAccount("Nora Nav", 67899, "GBP")

my_checking_account.print_balance()
my_checking_account.make_deposit(4000)
my_checking_account.make_withdrawal(100)
