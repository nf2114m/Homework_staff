import random

ACCOUNTS_FILE = "accounts.txt"

def load_accounts():
    accounts = {}
    try:
        f = open(ACCOUNTS_FILE, "r")
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                acc_num, name, balance = parts
                accounts[acc_num] = {"name": name, "balance": float(balance)}
        f.close()
    except FileNotFoundError:

    return accounts


def save_accounts(accounts):
    f = open(ACCOUNTS_FILE, "w")
    for acc_num in accounts:
        acc = accounts[acc_num]
        line = f"{acc_num},{acc['name']},{acc['balance']}\n"
        f.write(line)
    f.close()


def generate_account_number(accounts):
    while True:
        num = str(random.randint(100000, 999999))
        if num not in accounts:
            return num


def create_account(accounts):
    name = input("Enter your name: ")
    try:
        initial = float(input("Enter initial deposit: "))
        if initial < 0:
            print("Deposit must be non-negative.")
            return
    except ValueError:
        print("Invalid deposit amount.")
        return

    acc_num = generate_account_number(accounts)
    accounts[acc_num] = {"name": name, "balance": initial}
    save_accounts(accounts)
    print(f"Account created successfully. Your account number is {acc_num}")


def view_account(accounts):
    acc_num = input("Enter your account number: ")
    acc = accounts.get(acc_num)
    if acc:
        print(f"Name: {acc['name']}")
        print(f"Balance: ${acc['balance']:.2f}")
    else:
        print("Account not found.")


def deposit(accounts):
    acc_num = input("Enter your account number: ")
    acc = accounts.get(acc_num)
    if not acc:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            raise ValueError
        acc["balance"] += amount
        save_accounts(accounts)
        print("Deposit successful.")
    except ValueError:
        print("Invalid deposit amount.")


def withdraw(accounts):
    acc_num = input("Enter your account number: ")
    acc = accounts.get(acc_num)
    if not acc:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            raise ValueError
        if amount > acc["balance"]:
            print("Insufficient funds.")
            return
        acc["balance"] -= amount
        save_accounts(accounts)
        print("Withdrawal successful.")
    except ValueError:
        print("Invalid withdrawal amount.")


def main():
    accounts = load_accounts()
    while True:
        print("\n--- Simple Bank Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            view_account(accounts)
        elif choice == '3':
            deposit(accounts)
        elif choice == '4':
            withdraw(accounts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
