import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    fc = (df['low_fats'] == 'Y') & (df['recyclable'] == 'Y') # 2 filter  so use bracket
    return df[fc][['product_id']]  #  for returning in df insted of series use extra []

    