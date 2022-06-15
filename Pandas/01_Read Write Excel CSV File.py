import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv('stock_data.csv', nrows=3)
    print(df)
    df_NA = pd.read_csv('stock_data.csv', na_values={
        'eps': ['not available', 'n.a'],
        'revenue': ['-1']
    })  # replace specific values of not available to n.a, using dictionary
    df_NA.to_csv('stock_data_new.csv')  # Write new CSV file
    
    print(df_NA)
