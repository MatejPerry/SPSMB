from random import random

total_in = 0
total_tries = 0

for _ in range(1_000):
    x = random() - 0.5
    y = random() - 0.5

    if (x**2 + y**2) ** 0.5 < 0.5:
        total_in = total_in + 1

    total_tries = total_tries + 1

print(total_in / total_tries * 4)