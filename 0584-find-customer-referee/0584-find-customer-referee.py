import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer
    fc = (df['referee_id'] != 2) | (df['referee_id'].isnull())
    return df[fc][['name']]