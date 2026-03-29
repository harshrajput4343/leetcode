import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df1 = sales
    df2 = product

    df = pd.merge(left = df1, right = df2 , how = 'left', on = 'product_id')
    return df[['product_name','year', 'price']]
    