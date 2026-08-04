import pandas as pd

df = None

def load_csv(file_path):
    global df
    df = pd.read_csv(file_path)
    return df

def get_dataframe():
    return df