import pandas as pd

def read_files(path):
    df = pd.read_csv(path)
    return df