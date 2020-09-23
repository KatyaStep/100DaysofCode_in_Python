import collections

candles = [3, 2, 1, 3]

def birthdayCakeCandles(candles):
    highest_candle = max(candles)
    number_of_highest_candle = collections.Counter(candles)
    print(number_of_highest_candle[highest_candle])

birthdayCakeCandles(candles)