import random


def play_game(balance):
    print(f"Current balance: ${balance}")
    bet_amount = int(input("Place your bet amount: "))

    if bet_amount <= balance:
        balance -= bet_amount
        print("Spinning...")
    elif bet_amount > balance:
        print("INSUFFICIENT FUNDS NOOB")
        return None

    return balance


def print_symbols(slots):
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    slots.clear()
    for symbol in range(3):
        slots.append(random.choice(symbols))

    print(" | ".join(slots))
    if len(set(slots)) == 1:
        print()
        print("You win this round")
    elif len(set(slots)) > 1:
        print("Sorry you lost this round")
    # return [random.choice(symbols) for _ in range(3)] typecasting option to consider


def main():
    amount = 100
    slots = []
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while True:
        amount = play_game(amount)
        if amount == None:
            break
        print_symbols(slots)
        spin_again = input("Do you want to spin again? (Y/N): ").lower()
        if spin_again != "y":
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
