import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets
    fc = df['content'].str.len() > 15
    return df[fc][['tweet_id']]


    