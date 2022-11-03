
import statistics
from dataclasses import dataclass
from typing import Callable


@dataclass
class TradingBot:
    buy_strategy: Callable[[list[int]], bool]
    sell_strategy: Callable[[list[int]], bool]

    
    def run(self, prices: list[int]):
        if self.buy_strategy(prices):
            print("Just Buy.!")
        elif self.sell_strategy(prices):
            print("Just Sell.!")
        else:
            print("Do not buy or sell! Just observe.")
    

def should_buy_avg(prices: list[int]) -> bool:
    list_window = prices[-3:]
    return prices[-1] < statistics.mean(list_window)


def should_buy_minmax(prices: list[int]) -> bool:
    return prices[-1] < 32_000_00


def should_sell_avg(prices: list[int]) -> bool:
    list_window = prices[-3:]
    return prices[-1] > statistics.mean(list_window)

def should_sell_minmax(prices: list[int]) -> bool:
    return prices[-1] > 32_000_00



def main():
    prices = [52_550_00, 254_200_00, 120_000_00, 5_000_00, 12_800_00]
    bot = TradingBot(should_buy_avg, should_sell_avg)
    bot.run(prices)

if __name__ == "__main__":
    main()
