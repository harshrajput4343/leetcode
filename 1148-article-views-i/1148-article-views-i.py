import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views
    fc = df['author_id'] == df['viewer_id']
    return df[fc][['author_id']].drop_duplicates().sort_values(by = 'author_id').rename(columns = {'author_id' : 'id'})