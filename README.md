# Machine_Learning_Trader

# **Important Note** 
Please note that some code segments are intentionally redacted in compliance with school policy, with descriptions provided in their place. This information is shared for the purpose of demonstrating technical skills to potential employers and should not be publicly disclosed. Please be advised that this repository may only be available temporarily. Prospective employers are welcome to request access to the comprehensive codebase directly from the author.

The documentation intentionally omits detailed descriptions of functions and maintains a general project structure in this public repository. This approach is adopted to uphold the integrity of the instructional staff's efforts and prevent unauthorized duplication of the project.

## Environment Setup
The project's dependencies and environment specifications are outlined in the `environment.yaml` file included in the repository. The project was originally developed using a Miniconda environment on WSL2.

# Project Description: Algorithmic Trading Strategies

## Overview
This capstone project, conducted as part of a master's level course, delves into the implementation and comparison of two distinct trading strategies: a Manual Strategy and a Strategy Learner. The Manual Strategy, relying on human interpretation, incorporates indicators such as Bollinger Bands Percentage (BBP), Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), and Commodity Channel Index (CCI). The Strategy Learner, powered by a Random Forest classification model, autonomously develops trading rules using the same set of indicators.

## Objectives
1. Implement a class-based Manual Strategy that combines at least three out of five specified indicators.
2. Develop a class-based Strategy Learner using a Random Forest classification model, incorporating the same indicators as the Manual Strategy.
3. Rigorously test and debug both the Manual Strategy and Strategy Learner on specific symbol/time period scenarios.
4. Conduct experiments to compare the performance of the Manual Strategy and Strategy Learner. Evaluate the impact of varying market impact values on essential portfolio metrics.

## Plots
In the generated plots, blue lines signify the initiation of long positions, while black lines represent the initiation of short positions with the respective symbols. Notably, the strategy does not involve explicit position exits; instead, it swiftly transitions from long to short and vice versa.

## Conclusion
This capstone project provides valuable insights into the comparative performance of manual and AI-driven algorithmic trading strategies. It showcases adaptability to different market conditions and explores the impact of market parameters on overall portfolio outcomes.