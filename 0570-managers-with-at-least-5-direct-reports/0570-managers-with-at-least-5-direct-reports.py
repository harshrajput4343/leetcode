import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

        counts = employee['managerId'].value_counts()
    
    # managerIds with >= 5 reports
        valid_ids = counts[counts >= 5].index
    
    # filter employees whose id is in valid managerIds
        return employee[employee['id'].isin(valid_ids)][['name']]