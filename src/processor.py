import pandas as pd

CHUNK_SIZE = 100000

def process_data(file_path):
    for chunk in pd.read_csv(file_path, chunksize=CHUNK_SIZE, sep=','):
        chunk = transform(chunk)
        yield chunk

def transform(df):
    df["name"] = df["name"].fillna("Unknown")
    df["salary"] = df["salary"] * 1.1
    return df
