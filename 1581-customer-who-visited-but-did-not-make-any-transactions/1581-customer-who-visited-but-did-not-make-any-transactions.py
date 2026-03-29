import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df1 = visits
    df2 = transactions

    df = pd.merge(left = df1, right = df2 , how = 'left', on = 'visit_id')
    fc = df['transaction_id'].isnull()
    return df[fc].groupby('customer_id').agg({'visit_id':'count'}).reset_index().rename(columns= {'visit_id':'count_no_trans'})