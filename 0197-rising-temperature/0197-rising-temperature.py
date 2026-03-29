import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather
    df.sort_values(by = 'recordDate', inplace =True)
    df['prev_day_temp'] = df['temperature'].shift(1)
    df['prev_recordDate'] = df['recordDate'].shift(1)
    df['daysDiff'] = (df['recordDate'] - df['prev_recordDate']).dt.days
    fc = (df['temperature'] > df['prev_day_temp']) & (df['daysDiff'] == 1)
    return df[fc][['id']]
    