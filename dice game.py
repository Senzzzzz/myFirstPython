dices = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

dice = []
total = 0
user = int(input("How many dice?: "))

for die in range(user):
    dice.append(random.randint(1, 6))

for die in dice:
    total += die
    for rolls in dices[die]:
        print(rolls)
print(total)


current_balance = 0


def show_current_balance(balance):
    print(f"Current balance: ${balance:.2f}")


def deposit_money(balance):
    deposit_amount = int(input("Enter amount: "))
    balance += deposit_amount
    return balance


def withdraw_money(balance):
    withdraw_amount = int(input("Enter amount: "))
    balance -= withdraw_amount
    return balance


while True:
    show_balance = print("1.Show Balance")
    deposit = print("2.Deposit")
    withdraw = print("3.Withdraw")
    exit = print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    match choice:
        case "1": show_current_balance(current_balance)
        case "2": current_balance = deposit_money(current_balance)
        case "3": current_balance = withdraw_money(current_balance)
        case "4": break
        case _: print("Invalid option")
