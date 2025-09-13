import os

class BankAccount:
    def __init__(self, name, balance=None):
        self.name = name
        self.filename = f"{name}_account.txt"
        self.balance = 0.0

        # Load last known balance if file exists
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    if "New balance:" in line:
                        try:
                            self.balance = float(line.strip().split("New balance: ₹")[1])
                        except:
                            pass
        elif balance is not None:
            self.balance = balance
            self._log(f"🟢 Account created with ₹{balance}")

    def _log(self, message):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            msg = f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}"
            print(msg)
            self._log(msg)
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            msg = f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}"
            print(msg)
            self._log(msg)
        else:
            msg = f"❌ Failed withdrawal of ₹{amount} (Insufficient balance)"
            print(msg)
            self._log(msg)

    def show_details(self):
        print(f"\n👤 Account Holder: {self.name}")
        print(f"💰 Current Balance: ₹{self.balance}")
        print("📜 Transaction History:")
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    print(f"   - {line.strip()}")
        else:
            print("   No transactions found.")


# === Main Program ===
accounts = {}

while True:
    name = input("\nEnter employee name: ").strip()

    if name in accounts:
        account = accounts[name]
        print(f"👋 Welcome back, {name}!")
    elif os.path.exists(f"{name}_account.txt"):
        account = BankAccount(name)
        accounts[name] = account
        print(f"👋 Loaded existing account for {name} with ₹{account.balance}")
    else:
        raw_input = input("Enter initial deposit amount: ").strip()
        print(f"DEBUG: You entered '{raw_input}'")

        cleaned = raw_input.replace(",", ".")
        if cleaned.replace(".", "", 1).isdigit():
            initial_balance = float(cleaned)
            account = BankAccount(name, initial_balance)
            accounts[name] = account
            print(f"🎉 Account created for {name} with ₹{initial_balance}")
        else:
            print("❌ Please enter a valid number for the initial deposit.")
            continue

    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Account Details")
        print("4. Switch Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            amount_input = input("Enter amount to deposit: ").strip().replace(",", ".")
            if amount_input.replace(".", "", 1).isdigit():
                account.deposit(float(amount_input))
            else:
                print("❌ Invalid amount.")
        elif choice == '2':
            amount_input = input("Enter amount to withdraw: ").strip().replace(",", ".")
            if amount_input.replace(".", "", 1).isdigit():
                account.withdraw(float(amount_input))
            else:
                print("❌ Invalid amount.")
        elif choice == '3':
            account.show_details()
        elif choice == '4':
            break  # Switch employee
        elif choice == '5':
            print("👋 Thank you for using the Bank System!")
            exit()
        else:
            print("⚠️ Invalid choice. Please select from 1 to 5.")