import pandas as pd
import matplotlib.pyplot as plt
import os
DATA_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
def read_and_visualize():
    Apple_Inc = pd.read_csv(DATA_URL)
    print(Apple_Inc)
    count_row = Apple_Inc.shape[0]
    count_col = Apple_Inc.shape[1]
    print(count_row)
    print(count_col)
    print("Total rows:", count_row)
    print("Total columns:", count_col)
    plt.plot(Apple_Inc['AAPL_x'], Apple_Inc['AAPL_y'])
    plt.savefig('apple_stock.png')
    plt.close()
    return Apple_Inc

    
    
    
    
    
    
    