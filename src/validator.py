def validate(df):
    df = df[df["age"] > 18]
    df = df[df["salary"] > 0]
    return df
