import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df1 = employees
    df2 = employee_uni

    df = pd.merge(left = df1 , right = df2 , how = 'left', on = 'id')
    return df[['unique_id', 'name']]
    