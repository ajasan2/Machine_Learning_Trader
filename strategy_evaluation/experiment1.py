import marketsimcode as msc
import ManualStrategy as ms
import StrategyLearner as sl
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def author():
    return "ajasani9"

def conduct_experiment(symbol="JPM", commission=0.0, impact=0.0, sv=100000,
                    sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31)):

    # Redacted:
    # Generate trades dataframe using the manual strategy with a specified date range
    # Compute the portfolio values of manual trades, considering the initial investment value and other fees.
    # Set a benchmark strategy trades dataframe for the same stock symbol.
    # Compute the portfolio values of benchmark trades similar to before.

    slearn = sl.StrategyLearner(commission=commission, impact=impact)
    slearn.add_evidence(symbol=symbol, sd=dt.datetime(2008, 1, 1),
                        ed=dt.datetime(2009, 12, 31), sv=100000)

    learner_trades = slearn.testPolicy(symbol=symbol, sd=sd, ed=ed)
    learner_portval = msc.comp_portval(symbol=symbol, sd=sd, ed=ed, orders=learner_trades, start_val=sv,
                                       commission=commission, impact=impact)

    # Redacted normalization of all portfolio values

    fig, ax = plt.subplots()
    ax.plot(manual_portval.index, manual_portval, label="Manual Strategy", color="red")
    ax.plot(benchmark_portval.index, benchmark_portval, label="Benchmark", color="purple")
    ax.plot(learner_portval.index, learner_portval, label="Random Forest Learning Model", color="blue")

    # Redacted setting up plot components (axis label, legend, etc.)

