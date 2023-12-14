import numpy as np
import pandas as pd
import datetime as dt
import indicators as nd
from util import get_data


def author():
    return "ajasani9"


class ManualStategy:
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        self.verbose = verbose
        self.impact = impact
        self.commission = commission


    def testPolicy(
            self,
            symbol="JPM",
            sd=dt.datetime(2010, 1, 1),
            ed=dt.datetime(2011, 12, 31),
            sv=100000,
    ):
        price = get_data([symbol], pd.date_range(sd, ed)).drop(columns=["SPY"])

        ind = nd.Indicators()
        macd = ind.macd(symbol=symbol, sd=sd, ed=ed, short_window=5, long_window=35)
        bbp = ind.bbp(symbol=symbol, sd=sd, ed=ed, lookback=20)
        rsi = ind.rsi(symbol=symbol, sd=sd, ed=ed, lookback=14)
        cci = ind.cci(symbol=symbol, sd=sd, ed=ed, lookback=50)

        # Redacted logic to combine all indicator signals into a single signal

        trades = pd.DataFrame(data=0, index=price.index, columns=[symbol], dtype=int)
        net_holdings = 0

        for i in range(1, len(price)):
            if comb_ind[i - 1] > 1:
                if net_holdings == 0:
                    trades[symbol].iat[i] = 1000
                    net_holdings += 1000
                elif net_holdings < 0:
                    trades[symbol].iat[i] = 2000
                    net_holdings += 2000
            elif comb_ind[i - 1] < -1:
                if net_holdings == 0:
                    trades[symbol].iat[i] = -1000
                    net_holdings -= 1000
                elif net_holdings > 0:
                    trades[symbol].iat[i] = -2000
                    net_holdings -= 2000

        return trades

    def author(self):
        return "ajasani9"