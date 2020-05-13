# Encephalo Investments Coding Pre-Test - Revised April 2020

import pandas as pd
import numpy as np
import math


def cleanse_data(df):
    # Your task here is to remove data from any ticker that isn't XXY, sort chronologically and return a dataframe
    # whose only column is 'Adj Close'
    df = df[df.Ticker=='XXY']
    df = df.sort_values(by=['Date'])
    df = df.drop(columns = ['Ticker','Date'])
    dfclean = df
    return dfclean


def mc_sim(sims, days, df):
    # The code for a crude monte carlo simulation is given below. Your job is to extract the mean expected price
    # on the last day, as well as the 95% confidence interval.
    # Note that the z-score for a 95% confidence interval is 1.960
    returns = df.pct_change()
    last_price = df.iloc[-1]

    simulation_df = pd.DataFrame()

    for x in range(sims):
        count = 0
        daily_vol = returns.std()

        price_series = []

        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)

        for y in range(days):
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1

        simulation_df[x] = price_series
    
    expected_price = simulation_df.iloc[-1,0]['Adj Close']
    prices = []
    for index, row in simulation_df.iterrows():
        price = simulation_df.iloc[index,0]['Adj Close']
        prices.append(prices)
    prices = np.array(prices)
    prices = (prices-np.mean(prices))/np.std(prices)
    confidence = [price for price in prices if price>1.96]
    #confidence = simulation_df[x>1.96]
    # FILL OUT THE REST OF THE CODE. The above code has given you 'sims' of simulations run 'days' days into the future.
    # Your task is to return the expected price on the last day +/- the 95% confidence interval.
    return (expected_price,confidence)



def main():
    filename = '20192020histdata.csv'
    rawdata = pd.read_csv(filename)
    cleansed = cleanse_data(rawdata)
    simnum = 1  # change this number to one that you deem appropriate
    days = 25
    expected_price,confidence = mc_sim(simnum, days, cleansed)
    return




if __name__ == '__main__':
    main()
