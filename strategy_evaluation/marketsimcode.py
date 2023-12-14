import pandas as pd
import datetime as dt
from util import get_data


def author():
    return "ajasani9"


def get_metrics(prices=pd.DataFrame(), sv=1000000, sf=252.0):
    normed = prices / prices[0]
    port_val = normed * sv

    # Get portfolio statistics

    # Redacted getting daiy returns
    adr = dr.mean()
    sddr = dr.std()

    adj_fact = sf ** (1 / 2)
    # Redacted sharpe ratio calculation

    return cr, adr, sddr, sr


def comp_portval(
        symbol="APPL",
        sd=dt.datetime(2010, 1, 1),
        ed=dt.datetime(2011, 12, 31),
        orders=pd.DataFrame(),
        start_val=100000,
        commission=0.0,
        impact=0.0):

    prices = get_data([symbol], pd.date_range(sd, ed))
    prices = prices.drop(columns=["SPY"])
    prices["Cash"] = float(1)

    trades = prices.copy()
    for col in trades.columns:
        trades[col].values[:] = 0

    for index in orders.index:
        row = orders.loc[index]
        trades.at[index, "Cash"] -= commission

        # Redacted logic to keep track of total cash (whether on-hand or invested)

    holdings = trades.copy()
    holdings["Cash"].iat[0] += start_val
    for i in range(1, len(holdings)):
        holdings.iloc[i] += holdings.iloc[i - 1]

    values = prices * holdings
    return values.sum(axis=1)