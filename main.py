# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: ₹", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: ₹", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ₹", self.balance)

    def view_balance(self):
        print("Account balance: ₹", self.balance)

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    user = Bank(name, age, gender)

    while True:
        print("\n---- Bank Menu ----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            user.view_balance()
        elif choice == 4:
            print("Thank you for using the bank program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
