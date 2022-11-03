"""Trough this modul, we try to see how we can avoid a bunch of if-else 
statements by using dictionaries.
To achieve this we will replace the <should_by> function by the <simpler_should_by> function
"""
import statistics


def should_buy_avg(prices: list[int]) -> bool:
    list_window = prices[-3:]
    return prices[-1] < statistics.mean(list_window)


def should_buy_minmax(prices: list[int]) -> bool:
    return prices[-1] < 32_000_00


def should_buy_price_drop(prices: list[int]) -> bool:
    return prices[-1] < prices[-2]


def should_by(prices: list[int], strategy: str) -> bool:
    if strategy == "avg":
        return should_buy_avg(prices)
    elif strategy == "minmax":
        return should_buy_minmax(prices)
    elif strategy == "price_drop":
        return should_buy_price_drop(prices)
    else:
        raise ValueError(f"Unknown Strategy: {str}")


BUY_STRATEGIES = {"avg:": should_buy_avg, "minmax": should_buy_minmax, "price_drop": should_buy_price_drop}


def simpler_should_by(prices: list[int], strategy: str):
    return BUY_STRATEGIES[strategy](prices)


def main():
    prices = [52_550_00, 254_200_00, 120_000_00, 5_000_00, 12_800_00]
    print(f"Should buy: {simpler_should_by(prices=prices,strategy='price_drop')}")


if __name__ == "__main__":
    main()
