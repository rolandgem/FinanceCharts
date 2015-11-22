""" 
Created on November 20, 2015
@author: Roland Gemayel
@contact: rolandgemayel@gmail.com
Description: PricePlot.py downloads price data from Yahoo Finance and 
generates multiple price and returns plots to help you visualize the data.

Inputs: symbols_list, dt_start, dt_end, t0, t1
Outputs: AdjustedClose.png, NormalizedClose.png, DailyReturns.png, ScatterPlot.png
Libraries: Requires pandas_datareader to be installed. In terminal paste "pip install pandas-datareader"
"""

import numpy as np 
import pandas as pd 
import datetime as dt 
import matplotlib
import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader


def PricePlot():
	## Define what you want to study and over what period
	
	# List of symbols
	symbols_list = ['AA', 'AAPL', 'MCD', 'YHOO']

	# Start and End dates
	dt_start = dt.datetime(2012, 1,1)
	dt_end = dt.datetime(2015, 1,1)

	# Download historical Adjusted Closing prices using Pandas downloader for Yahoo: pandas.io.data.DataReader
	data = DataReader(symbols_list, 'yahoo', dt_start, dt_end)['Adj Close']

	# Plotting Adj Closing prices with x-axis = time. Saves chart as png in directory.
	plt.clf()
	plt.plot(data)
	plt.legend(symbols_list)
	plt.ylabel('Adjusted Close')
	plt.xlabel('Date')
	matplotlib.rcParams.update({'font.size': 8})
	plt.savefig('AdjustedClose.png', format='png')

	# Normalizing prices to start at 1 to visualize relative value over time.
	data_normalized = data/data.iloc[0]
	plt.clf()
	plt.plot(data_normalized)
	plt.legend(symbols_list)
	plt.ylabel('Normalized Close')
	plt.xlabel('Date')
	matplotlib.rcParams.update({'font.size': 8})
	plt.savefig('NormalizedClose.png', format='png')

	# Plotting returns over 30 days starting after t0=10 days and ending at t1=40
	# First create dataframe data_ret which includes returns
	data_ret = data/data.shift(1) - 1
	t0=10
	t1=40

	# Plot Daily returns
	plt.clf()
	plt.plot(data_ret[t0:t1])
	plt.axhline(y=0, color='b')
	plt.legend(symbols_list)
	plt.ylabel('Daily Returns')
	plt.xlabel('Date')
	matplotlib.rcParams.update({'font.size': 8})
	plt.savefig('DailyReturns.png', format='png')

	# Scatter plot of two stocks AA and AAPL
	plt.clf()
	plt.scatter(data_ret['AA'], data_ret['AAPL'], c='green')
	plt.xlabel('AA')
	plt.ylabel('AAPL')
	matplotlib.rcParams.update({'font.size': 8})
	plt.savefig('ScatterPlot.png', format='png')

PricePlot()










