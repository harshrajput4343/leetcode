import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
       # Precompute boolean flag (vectorized)
    confirmations['is_confirmed'] = (confirmations['action'] == 'confirmed').astype(int)
    
    # Aggregate confirmations table first
    agg = confirmations.groupby('user_id').agg(
        confirmed=('is_confirmed', 'sum'),
        total=('action', 'count')
    ).reset_index()
    
    # Left join with signups
    result = signups.merge(agg, on='user_id', how='left')
    
    # Fill missing users (no confirmations)
    result[['confirmed', 'total']] = result[['confirmed', 'total']].fillna(0)
    
    # Compute rate
    result['confirmation_rate'] = (result['confirmed'] / result['total']).fillna(0).round(2)
    
    return result[['user_id', 'confirmation_rate']]