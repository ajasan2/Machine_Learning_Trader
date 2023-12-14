import StrategyLearner as sl
import datetime as dt
import matplotlib.pyplot as plt
import marketsimcode as msc


def author():
    return "ajasani9"


def conduct_experiment(symbol="JPM", commission=0.0, impact=[], sv=100000,
                    sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31)):

    # Redacted managing each set of portfolio values and its standard deviation
    for i in impact:
        slearn = sl.StrategyLearner(commission=commission, impact=i)
        slearn.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=sv)
        trades = slearn.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)
        portval = msc.comp_portval(symbol=symbol, sd=sd, ed=ed, orders=trades, commission=commission, impact=i)

    # Redacted getting portfolio values for each impact value being tested
    plt.title("Portfolio Value for Different Impact Values")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.legend()
    plt.savefig("exp2_pv.png", dpi=300, bbox_inches="tight")

    # Create a bar graph for impact value and the corresponding standard deviation
    # Redacted specific graph visualization code
    plt.clf()
    plt.figure()
    plt.xlabel("Impact Values")
    plt.ylabel("Standard Deviation of Daily Returns")
    plt.title("Portfolio Volatility for Different Impact Values")
    plt.xticks(impact)
    plt.savefig("exp2_sddr.png", dpi=300, bbox_inches="tight")
