class Checkbook:
    # Initialize a new Checkbook instance.
    def __init__(self):
        self.balance = 0.0

    # Deposit an amount to the checkbook.
    # amount (float): The amount to deposit.
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Withdraw an amount from the checkbook.
    # amount (float): The amount to withdraw.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Print the current balance of the checkbook.
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# The main function that runs the checkbook program.
def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
