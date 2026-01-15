import pandas as pd
import matplotlib.pyplot as plt
import os
DATA_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
def read_and_visualize():
    df = pd.read_csv(DATA_URL)
    print(df)
    count_row = df.shape[0]
    count_col = df.shape[1]
    print(count_row)
    print(count_col)
    print("Total rows:", count_row)
    print("Total columns:", count_col)
    plt.plot(df["AAPL_x"], df["AAPL_y"], label="Stock Prices")
    plt.savefig("apple_stock.png")
    plt.close()
    return df
def calculate_moving_average(df, window_size=30):
    df_SMA = df["AAPL_y"].rolling(window=window_size).mean()
    
    plt.plot(df["AAPL_x"], df["AAPL_y"], label="Stock Prices")
    plt.plot(df['AAPL_x'], df_SMA, label=f"SMA ({window_size})")
    plt.legend()
    plt.savefig("apple_stock_sma.png")
    plt.close()
    
    return df

#df = read_and_visualize()
#df = calculate_moving_average(df, window_size=30)


    

    
    
    
    
    
    
    