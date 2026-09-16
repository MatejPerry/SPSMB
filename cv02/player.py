from random import random, choice
from dataclasses import dataclass


# ============================================================
# HRA
# ============================================================

COLORS = {
    0: "Red",
    1: "White",
    2: "Green"
}


def get_color():
    """
    Vylosuje výsledek:
    Red   = 48.5 %
    White = 48.5 %
    Green = 3 %
    """
    value = random() * 100

    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1


# ============================================================
# HRÁČ
# ============================================================

@dataclass
class Player:
    balance: float
    wins: int = 0
    losses: int = 0
    total_bet: float = 0
    biggest_balance: float = 0
    smallest_balance: float = 0

    def __post_init__(self):
        self.biggest_balance = self.balance
        self.smallest_balance = self.balance


# ============================================================
# STRATEGIE
# ============================================================

def random_color_strategy():
    """Hráč náhodně vybere barvu."""
    return choice([0, 1, 2])


def red_strategy():
    """Hráč vždy sází na červenou."""
    return 0


def white_strategy():
    """Hráč vždy sází na bílou."""
    return 1


def green_strategy():
    """Hráč vždy sází na zelenou."""
    return 2


def random_bet_strategy(balance):
    """Sází 10 % aktuálního bankrollu."""
    return max(1, int(balance * 0.10))


def fixed_bet_strategy(balance):
    """Vždy sází 10 EUR, pokud na ně má."""
    return min(10, int(balance))


# ============================================================
# JEDNO KOLO
# ============================================================

def play_round(player, color_strategy, bet_strategy):

    if player.balance <= 0:
        return False

    bet = bet_strategy(player.balance)

    if bet <= 0:
        return False

    selection = color_strategy()
    result = get_color()

    player.total_bet += bet

    # Sázka se nejprve odečte
    player.balance -= bet

    if selection == result:

        # Výhra 2:1
        player.balance += bet * 3

        player.wins += 1

    else:
        player.losses += 1

    player.biggest_balance = max(
        player.biggest_balance,
        player.balance
    )

    player.smallest_balance = min(
        player.smallest_balance,
        player.balance
    )

    return True


# ============================================================
# SIMULACE JEDNOHO HRÁČE
# ============================================================

def simulate_player(
    starting_balance=1_000,
    rounds=10_000,
    color_strategy=random_color_strategy,
    bet_strategy=random_bet_strategy
):

    player = Player(starting_balance)

    for _ in range(rounds):

        if not play_round(
            player,
            color_strategy,
            bet_strategy
        ):
            break

    return player


# ============================================================
# SIMULACE VÍCE HRÁČŮ
# ============================================================

def simulate(
    players_count=10_000,
    starting_balance=1_000,
    rounds=1_000,
    color_strategy=random_color_strategy,
    bet_strategy=random_bet_strategy
):

    players = []

    for _ in range(players_count):

        player = simulate_player(
            starting_balance,
            rounds,
            color_strategy,
            bet_strategy
        )

        players.append(player)

    return players


# ============================================================
# STATISTIKY
# ============================================================

def print_statistics(players, starting_balance):

    bankrupt = 0
    profitable = 0

    total_start = 0
    total_end = 0

    total_wins = 0
    total_losses = 0
    total_bets = 0

    biggest_balance = 0
    smallest_balance = float("inf")

    for player in players:

        total_start += starting_balance
        total_end += player.balance

        total_wins += player.wins
        total_losses += player.losses
        total_bets += player.total_bet

        biggest_balance = max(
            biggest_balance,
            player.biggest_balance
        )

        smallest_balance = min(
            smallest_balance,
            player.smallest_balance
        )

        if player.balance <= 0:
            bankrupt += 1

        if player.balance > starting_balance:
            profitable += 1

    player_count = len(players)

    print()
    print("=" * 50)
    print("SIMULATION RESULTS")
    print("=" * 50)

    print(f"Players:              {player_count:,}")
    print(f"Starting balance:     {starting_balance:,.2f} EUR")
    print(f"Total starting money: {total_start:,.2f} EUR")
    print(f"Total final money:    {total_end:,.2f} EUR")

    print()
    print(f"Casino result:        {total_start - total_end:,.2f} EUR")

    print()
    print(f"Bankrupt players:     {bankrupt:,}")
    print(
        f"Bankruptcy rate:      "
        f"{bankrupt / player_count * 100:.2f}%"
    )

    print(
        f"Players in profit:    "
        f"{profitable:,}"
    )

    print(
        f"Profit rate:          "
        f"{profitable / player_count * 100:.2f}%"
    )

    print()
    print(f"Total wins:           {total_wins:,}")
    print(f"Total losses:         {total_losses:,}")
    print(f"Total money bet:      {total_bets:,.2f} EUR")

    print()
    print(f"Highest balance:      {biggest_balance:,.2f} EUR")
    print(f"Lowest balance:       {smallest_balance:,.2f} EUR")

    print("=" * 50)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    players = simulate(
        players_count=10_000,
        starting_balance=1_000,
        rounds=1_000,

        # Strategie barvy:
        color_strategy=random_color_strategy,

        # Strategie sázky:
        bet_strategy=random_bet_strategy
    )

    print_statistics(
        players,
        starting_balance=1_000
    )
