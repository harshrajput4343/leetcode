import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world
    fc = (df['area'] >= 3000000 ) | (df['population'] >= 25000000)
    return df[fc][['name', 'population', 'area']]