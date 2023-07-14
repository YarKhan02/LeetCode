import random

def coin_change(coins, amount):
    r = len(coins)
    t = [[0 if i == 0 and j != 0 else 1 if i != 0 and j == 0 else 0 for j in range(amount + 1)] for i in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                t[i][j] = t[i][j - coins[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[r][amount]


coins = [1, 2, 5]
n = 5

print(coin_change(coins, n))