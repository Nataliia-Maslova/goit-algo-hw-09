import timeit

def find_coins_greedy(amount, coins):
    coins_count = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            coins_count[coin] = count
        amount -= coin * count
    return coins_count

if __name__ == '__main__':
    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([10, 6, 1], 12),
        ([25, 10, 5, 2, 1], 543210)
    ]

    functions = [find_coins_greedy]

    for coins, amount in cases:
        print(f"\nCase for {coins} and sum: {amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(amount, coins), number=10000)
            print(f"Result for {fun.__name__}: {fun(amount, coins)}")
            print(f"Time taken for {fun.__name__}: {time:.6f} seconds")


def find_min_coins(amount, coins):
# Ініціалізує список min_coins_required нескінченністю, за винятком нульової суми
    min_coins_required = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

# Повернення назад, щоб знайти монети, використані для формування суми
    coins_count = {}
    current_sum = amount
    while current_sum > 0:
        coin = coin_used[current_sum]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        current_sum -= coin

    return coins_count

if __name__ == '__main__':
    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([10, 6, 1], 12),
        ([25, 10, 5, 2, 1], 543210)
    ]

    functions = [find_min_coins]

    for coins, amount in cases:
        print(f"\nCase for {coins} and sum: {amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(amount, coins), number=1)
            print(f"Result for {fun.__name__}: {fun(amount, coins)}")
            print(f"Time taken for {fun.__name__}: {time:.6f} seconds")
