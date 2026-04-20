from sqlalchemy import create_engine

engine = create_engine("sqlite:///data.db")

def load_to_db(df):
    df.to_sql("employees", con=engine, if_exists="append", index=False)


