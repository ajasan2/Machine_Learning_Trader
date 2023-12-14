""""""
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  

Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  

Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  

We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  

-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  	   		  		 		  		  		    	 		 		   		 		  	  	   		  		 		  		  		    	 		 		   		 		  
"""

import numpy as np
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import indicators as nd
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data
import RTLearner as rl
import BagLearner as bl

def author():
    return "ajasani9"


class StrategyLearner(object):
    # constructor  		  	   		  		 		  		  		    	 		 		   		 		  
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        # Redacted class setup

    def add_evidence(  		  	   		  		 		  		  		    	 		 		   		 		  
        self,  		  	   		  		 		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        ed=dt.datetime(2009, 12, 31),
        sv=10000,  		  	   		  		 		  		  		    	 		 		   		 		  
    ):

        price = get_data([symbol], pd.date_range(sd, ed)).drop(columns=["SPY"])

        # Redacted extraction of indicators

        nd_forecast = 2
        y_targ = np.zeros(all_indicators.shape[0] - nd_forecast)

        for i in range(len(y_targ)):

            # Redacted calculation of potential return

            if nd_ret > 0.01:
                y_targ[i] = 1000
            elif nd_ret < -0.01:
                y_targ[i] = -1000

        # Redacted evidence gathering


    def testPolicy(
        self,  		  	   		  		 		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2009, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        ed=dt.datetime(2010, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        sv=100000,
    ):

        # Redacted extraction of indicators

        trades_arr = self.bags.query(all_indicators)

        # Redacted modifications to generated trading orders

        return pd.DataFrame(trades_arr, index=macd.index, columns=[symbol])


    def author(self):
        return "ajasani9"