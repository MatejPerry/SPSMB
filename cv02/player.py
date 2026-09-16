from random import random, choice


def get_color():
    value = random() * 100

    if value <= 3:
        return 2       # Green
    elif value <= 51.5:
        return 0       # Red
    else:
        return 1       # White


def simulate_player(start_balance=1_000, rounds=100_000):
    balance = start_balance

    colors = {
        0: "Red",
        1: "White",
        2: "Green"
    }

    for round_number in range(1, rounds + 1):

        # Hráč vsadí např. 10 % aktuálního zůstatku
        bet = max(1, int(balance * 0.10))

        # Náhodně vybere barvu
        selection = choice([0, 1, 2])

        result = get_color()

        if selection == result:
            balance += bet * 2
        else:
            balance -= bet

        # Hráč zkrachoval
        if balance <= 0:
            print(f"Hráč zkrachoval v kole {round_number}.")
            balance = 0
            break

        # Průběžný výpis
        if round_number % 10_000 == 0:
            print(
                f"Kolo {round_number}: "
                f"balance = {balance} EUR"
            )

    print("\n--- Výsledek ---")
    print(f"Počáteční balance: {start_balance} EUR")
    print(f"Konečná balance:   {balance} EUR")
    print(f"Rozdíl:             {balance - start_balance} EUR")
    print(f"Odehráno kol:       {round_number}")


if __name__ == "__main__":
    simulate_player()
