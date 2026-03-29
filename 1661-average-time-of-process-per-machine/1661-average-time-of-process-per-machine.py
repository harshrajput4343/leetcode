import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df_start =df[ df['activity_type'] == 'start']
    df_end = df[ df['activity_type']== 'end']
    final_df = pd.merge(left = df_start, right = df_end , how = 'inner', on = ['machine_id', 'process_id'])
    final_df['processing_time'] = final_df['timestamp_y'] - final_df['timestamp_x']
    return final_df.groupby('machine_id').agg({'processing_time':'mean'}).reset_index().round(3)
    