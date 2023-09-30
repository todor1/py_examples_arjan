# https://www.youtube.com/watch?v=ph2HjBQuI8Y&ab_channel=ArjanCodes
import statistics
from dataclasses import dataclass
from typing import Callable, Protocol
from functools import partial

from exchange import Exchange

# # ------------------------------------------------------------------------------
### Functional implementation with Partial functions 
# # ------------------------------------------------------------------------------
TradingStrategyFunction = Callable[[list[int]], bool]

def should_buy_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)

def should_sell_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)

def should_buy_minmax(prices: list[int], max_price: float) -> bool:            
    return prices[-1] < max_price

def should_sell_minmax(prices: list[int], min_price: float) -> bool:        
    return prices[-1] > min_price


@dataclass
class TradingBot:
    """Trading bot that connects to exchange and performs trades
        Create partially applied versions of the trading functions
    """ 
    exchange: Exchange
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction
    
    def run(self, symbol:str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)
        if should_buy:
            self.exchange.buy(symbol=symbol, amount=10)
        elif should_sell:
            self.exchange.sell(symbol=symbol, amount=10)
        else:
            print(f"No action needed for {symbol}.")
            
            
def main() -> None:
    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()    
    # create the trading bot and run the bot once
    # Create partially applied versions of the trading functions
    buy_strategy = partial(should_buy_avg, window_size=4)
    sell_strategy = partial(should_sell_minmax, min_price=32_000_00)
    bot = TradingBot(exchange, buy_strategy, sell_strategy)
    bot.run("BTC/USD")
    

# # # ------------------------------------------------------------------------------
# ### Functional implementation with closures - passing parameters to functions
# # # ------------------------------------------------------------------------------
# TradingStrategyFunction = Callable[[list[int]], bool]

# def should_buy_avg_closure(window_size: int) -> TradingStrategyFunction:
#     def should_buy_avg(prices: list[int]) -> bool:
#         list_window = prices[-window_size:]
#         return prices[-1] < statistics.mean(list_window)
#     return should_buy_avg


# def should_sell_avg_closure(window_size: int) -> TradingStrategyFunction:
#     def should_sell_avg(prices: list[int]) -> bool:
#         list_window = prices[-window_size:]
#         return prices[-1] > statistics.mean(list_window)
#     return should_sell_avg


# def should_buy_minmax_closure(max_price: float) -> TradingStrategyFunction:
#     def should_buy_minmax(prices: list[int]) -> bool:            
#         return prices[-1] < max_price
#     return should_buy_minmax


# def should_sell_minmax_closure(max_price: float) -> TradingStrategyFunction:
#     def should_sell_minmax(prices: list[int]) -> bool:        
#         return prices[-1] > max_price
#     return should_sell_minmax


# @dataclass
# class TradingBot:
#     """Trading bot that connects to exchange and performs trades""" 
#     exchange: Exchange
#     buy_strategy: TradingStrategyFunction
#     sell_strategy: TradingStrategyFunction
    
#     def run(self, symbol:str) -> None:
#         prices = self.exchange.get_market_data(symbol)
#         should_buy = self.buy_strategy(prices)
#         should_sell = self.sell_strategy(prices)
#         if should_buy:
#             self.exchange.buy(symbol=symbol, amount=10)
#         elif should_sell:
#             self.exchange.sell(symbol=symbol, amount=10)
#         else:
#             print(f"No action needed for {symbol}.")
            
            
# def main() -> None:
#     # create the exchange and connect to it
#     exchange = Exchange()
#     exchange.connect()    
#     # create the trading bot and run the bot once
#     # bot = TradingBot(exchange, should_buy_avg_closure(window_size=4), should_sell_minmax_closure(max_price=30_000_45))
#     # bot = TradingBot(exchange, should_buy_avg_closure(window_size=1), should_sell_minmax_closure(max_price=35_000_45))
#     bot = TradingBot(exchange, should_buy_avg_closure(window_size=6), should_sell_avg_closure(window_size=7))
#     bot.run("BTC/USD")

# # # ---------------------------------------------------------
# ### Functional implementation
# # # ---------------------------------------------------------
# TradingStrategyFunction = Callable[[list[int]], bool]

# def should_buy_avg(prices: list[int]) -> bool:
#     list_window = prices[-3:]
#     return prices[-1] < statistics.mean(list_window)

# def should_sell_avg(prices: list[int]) -> bool:
#     list_window = prices[-3:]
#     return prices[-1] > statistics.mean(list_window)


# def should_buy_minmax(prices: list[int]) -> bool:        
#     # buy if it's below $32,000
#     return prices[-1] < 32_000_00

# def should_sell_minmax(prices: list[int]) -> bool:
#     # sell if it's above $32,000
#     return prices[-1] > 32_000_00


# @dataclass
# class TradingBot:
#     """Trading bot that connects to exchange and performs trades""" 
#     exchange: Exchange
#     buy_strategy: TradingStrategyFunction
#     sell_strategy: TradingStrategyFunction
    
#     def run(self, symbol:str) -> None:
#         prices = self.exchange.get_market_data(symbol)
#         should_buy = self.buy_strategy(prices)
#         should_sell = self.sell_strategy(prices)
#         if should_buy:
#             self.exchange.buy(symbol=symbol, amount=10)
#         elif should_sell:
#             self.exchange.sell(symbol=symbol, amount=10)
#         else:
#             print(f"No action needed for {symbol}.")
            
            
# def main() -> None:
#     # create the exchange and connect to it
#     exchange = Exchange()
#     exchange.connect()    
#     # create the trading bot and run the bot once
#     # bot = TradingBot(exchange, should_buy_avg, should_sell_avg)
#     # bot = TradingBot(exchange, should_buy_minmax, should_sell_minmax)
#     # Using the functional approach we can apply different strategies
#     # bot = TradingBot(exchange, should_buy_avg, should_sell_minmax)
#     bot = TradingBot(exchange, should_buy_minmax, should_sell_avg)
#     bot.run("BTC/USD")


# # ---------------------------------------------------------
# # Traditional OOP implementation of the Strategy Pattern: 
# # - an abstract class (protocol class) defining the interface
# # - subclasses that implement the protocol
# # - another class that uses the above structures (TradingBot)
# # ---------------------------------------------------------


# class TradingStrategy(Protocol):
#     """Trading strategy that defines whether to buy or sell, given a list of prices.
#     """
    
#     def should_buy(self, prices: list[int]) -> bool:
#         raise NotImplementedError()
    
#     def should_sell(self, prices: list[int]) -> bool:
#         raise NotImplementedError()
    
    
# class AverageTradingStrategy:
#     """Trading strategy based on price averages."""
    
#     def should_buy(self, prices: list[int]) -> bool:
#         list_window = prices[-3:]
#         return prices[-1] < statistics.mean(list_window)

#     def should_sell(self, prices: list[int]) -> bool:
#         list_window = prices[-3:]
#         return prices[-1] > statistics.mean(list_window)

    
# class MinMaxTradingStrategy:
#     """Trading strategy based on price minima and maxima."""
    
#     def should_buy(self, prices: list[int]) -> bool:        
#         # buy if it's below $32,000
#         return prices[-1] < 32_000_00

#     def should_sell(self, prices: list[int]) -> bool:
#         # sell if it's above $32,000
#         return prices[-1] > 32_000_00
            
    
# @dataclass
# class TradingBot:
#     """Trading bot that connects to exchange and performs trades""" 
#     exchange: Exchange
#     trading_strategy: TradingStrategy
    
#     def run(self, symbol:str) -> None:
#         prices = self.exchange.get_market_data(symbol)
#         should_buy = self.trading_strategy.should_buy(prices)
#         should_sell = self.trading_strategy.should_sell(prices)
#         if should_buy:
#             self.exchange.buy(symbol=symbol, amount=10)
#         elif should_sell:
#             self.exchange.sell(symbol=symbol, amount=10)
#         else:
#             print(f"No action needed for {symbol}.")
        

# def main() -> None:
#     # create the exchange and connect to it
#     exchange = Exchange()
#     exchange.connect()
#     # create the trading strategy
#     # trading_strategy = MinMaxTradingStrategy()
#     trading_strategy = AverageTradingStrategy()
#     # create the trading bot and run the bot once
#     bot = TradingBot(exchange, trading_strategy)
#     bot.run("BTC/USD")

# # ---------------------------------------------------------
### Traditional OOP implementation of the Strategy Pattern: 
# # ---------------------------------------------------------
    
    
if __name__ == "__main__":
    main()