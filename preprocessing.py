import pandas as pd
import string
import os


def process_likes(file_name):
    df = pd.read_csv(file_name)
    for i in range(0, df.shape[0]):
        a, b = (df.iloc[i, 2]).split('REPLY')
        df.iloc[i, 2] = a
    for i in range(0, df.shape[0]):
        if df.iloc[i, 2] == '':
            df.iloc[i, 2] = 0
    for i in range(0, df.shape[0]):
        df.iloc[i, 2] = str(df.iloc[i, 2]).rstrip()
    for i in range(0, df.shape[0]):
        try:
            df.iloc[i, 2] = int(df.iloc[i, 2])
        except:
            a = df.iloc[i, 2]
            try:
                df.iloc[i, 2] = float(a.split('M')[0]) * 1000000
            except:
                df.iloc[i, 2] = float(a.split('K')[0]) * 1000

    df.to_csv(file_name)

