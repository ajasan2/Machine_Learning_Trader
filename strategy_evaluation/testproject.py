import marketsimcode as msc
import ManualStrategy as ms
import StrategyLearner as sl
import pandas as pd
import datetime as dt
import random
import matplotlib.pyplot as plt
import experiment1 as exp1
import experiment2 as exp2
from pandas.plotting import register_matplotlib_converters


def plot_results(trades, portval, benchmark):
    fig, ax = plt.subplots()
    ax.plot(trades.index, portval, label="Manual Strategy", color="red")
    ax.plot(trades.index, benchmark, label="Benchmark", color="purple")

    # Plotting vertical lines for entry points
    for date, trade in trades.iterrows():
        amount = trade.iat[0]
        if amount == 1000 or amount == 2000:

        # Redacted part of vertical line visualization that indicated entry position on plot

    ax.set_xlim(trades.index[0], trades.index[-1])
    plt.title(f"Benchmark vs. Manual Strategy")
    plt.xlabel("Date")
    plt.xticks(rotation=30)
    plt.ylabel("Normalized Portfolio Value")
    plt.legend(loc='upper left')


def manual_strategy(symbol="JPM", commission=0.0, impact=0.0, sv=100000,
                    sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31)):
    # Redacted:
    # Generate trades dataframe using the manual strategy with a specified date range
    # Compute the portfolio values of manual trades, considering the initial investment value and other fees.
    # Set a benchmark strategy trades dataframe for the same stock symbol.
    # Compute the portfolio values of benchmark trades similar to before.

    cr, adr, sddr, _ = msc.get_metrics(prices=portval, sv=sv)
    b_cr, b_adr, b_sddr, _ = msc.get_metrics(prices=benchmark_portval, sv=sv)
    with open("p8_results.txt", "a") as f:
        print(f"====================== {sd} to {ed} ======================", file=f)
        print(f"Cumulative Returns _____________________ Benchmark: {b_cr:.4f} | Manual: {cr:.4f}", file=f)
        print(f"Average Daily Returns __________________ Benchmark: {b_adr:.4f} | Manual: {adr:.4f}", file=f)
        print(f"Standard Deviation of Daily Returns ____ Benchmark: {b_sddr:.4f} | Manual: {sddr:.4f}\n", file=f)

    # Redacted modifications to arguments prior to function call
    plot_results(trades, portval, benchmark_portval)


def evaluate_strategy(learner, symbol, start_date, end_date, label, num_trials):
    total_returns = 0
    benchmark_portval = None

    # Redacted loop that executes multiple runs of the strategy

    average_return = total_returns / num_trials
    print("{}: {:+.4f} | {}: {:+.4f}".format("Benchmark", benchmark_portval[-1]/benchmark_portval[0]-1, label, average_return))


def learn_strategy(symbol="JPM"):
    slearn = sl.StrategyLearner()
    slearn.add_evidence(symbol=symbol, sd=dt.datetime(2008, 1, 1),
                        ed=dt.datetime(2009, 12, 31), sv=100000)

    # IN_SAMPLE
    evaluate_strategy(learner=slearn, symbol=symbol, start_date=dt.datetime(2008, 1, 1),
                      end_date=dt.datetime(2009, 12, 31), label='IN_SAMPLE', num_trials=1)

    # OUT_OF_SAMPLE
    evaluate_strategy(learner=slearn, symbol=symbol, start_date=dt.datetime(2010, 1, 1),
                      end_date=dt.datetime(2011, 12, 31), label='OUT_OF_SAMPLE', num_trials=1)


if __name__ == "__main__":
    register_matplotlib_converters()
    # Redacted main entry points into appropriate functions to meet project requirements
