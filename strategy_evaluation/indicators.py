import pandas as pd
import datetime as dt
from util import get_data


def author():
    return "ajasani9"


def calculate_ema(data, window):
    multiplier = 2 / (window + 1)
    ema = pd.Series(index=data.index, dtype=float)
    ema.iloc[window - 1] = data.iloc[:window].mean()

    # Redacted ema calculation

    return ema


class Indicators:
    def macd(self, symbol="JPM",
             sd=dt.datetime(2008, 1, 1),
             ed=dt.datetime(2009, 12, 31),
             short_window=12,
             long_window=26):
        mod_sd = sd - pd.DateOffset(days=2 * long_window)
        prices = get_data([symbol], pd.date_range(mod_sd, ed)).drop(columns=["SPY"])

        ema_short = calculate_ema(prices[symbol], short_window)
        ema_long = calculate_ema(prices[symbol], long_window)

        macd = ema_short - ema_long
        return macd[sd:]

    def bbp(self, symbol="JPM",
            sd=dt.datetime(2008, 1, 1),
            ed=dt.datetime(2009, 12, 31),
            lookback=20):

        mod_sd = sd - pd.DateOffset(days=2 * lookback)
        prices = get_data([symbol], pd.date_range(mod_sd, ed)).drop(columns=["SPY"])

        sma = prices[symbol].rolling(window=lookback).mean()
        stdev = prices[symbol].rolling(window=lookback).std()

        upper_band = sma + 2 * stdev
        lower_band = sma - 2 * stdev

        # Redacted bbp conversion to single vector
        return bbp[sd:]


    def momentum(self, symbol="JPM",
             sd=dt.datetime(2008, 1, 1),
             ed=dt.datetime(2009, 12, 31),
             lookback=20):

        mod_sd = sd - pd.DateOffset(days=2 * lookback)
        prices = get_data([symbol], pd.date_range(mod_sd, ed)).drop(columns=["SPY"])

        prices["prev_price"] = prices[symbol].shift(lookback)  # Close n periods ago
        momentum = (prices[symbol] - prices["prev_price"]) - 1
        return momentum[sd:]

    def rsi(self, symbol="JPM",
            sd=dt.datetime(2008, 1, 1),
            ed=dt.datetime(2009, 12, 31),
            lookback=14):

        mod_sd = sd - pd.DateOffset(days=2 * lookback)
        prices = get_data([symbol], pd.date_range(mod_sd, ed)).drop(columns=["SPY"])

        # Redacted finding trading days resulting in gains and losses

        avg_gain = gains.rolling(window=lookback).mean()
        avg_loss = losses.rolling(window=lookback).mean()

        # Redacted RSI calculations
        return rsi[sd:].squeeze()

    def cci(self, symbol="JPM",
            sd=dt.datetime(2008, 1, 1),
            ed=dt.datetime(2009, 12, 31),
            lookback=20):
        mod_sd = sd - pd.DateOffset(days=3 * lookback)
        close = get_data(symbols=[symbol], dates=pd.date_range(mod_sd, ed), colname="Close").drop(columns=["SPY"])
        adj_close = get_data(symbols=[symbol], dates=pd.date_range(mod_sd, ed), colname="Adj Close").drop(
            columns=["SPY"])
        high = get_data(symbols=[symbol], dates=pd.date_range(mod_sd, ed), colname="High").drop(columns=["SPY"])
        low = get_data(symbols=[symbol], dates=pd.date_range(mod_sd, ed), colname="Low").drop(columns=["SPY"])

        # Redacted adjusting high and low values to match adjustment of closing values

        tp_price = (adj_high + adj_low + adj_close) / 3
        sma_tp_price = tp_price.rolling(window=lookback).mean()
        diff = tp_price - sma_tp_price

        # Redacted CCI calculations

        return cci[sd:].squeeze()
