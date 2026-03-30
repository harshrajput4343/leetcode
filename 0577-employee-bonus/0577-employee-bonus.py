import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df1 = employee
    df2 = bonus

    df = pd.merge(left = df1, right = df2, how = 'left', on = 'empId')
    fc = (df['bonus'] < 1000) | df['bonus'].isnull()
    return df[fc][['name','bonus']]

    