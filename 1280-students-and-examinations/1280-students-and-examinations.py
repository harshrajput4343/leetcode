import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations['attended_exams'] = 1
    df = pd.merge(left= students, right = subjects , how = 'cross')
    df_final= pd.merge(left = df, right = examinations, how = 'left', on = ['student_id','subject_name'])
    return df_final.groupby(['student_id','student_name','subject_name'],dropna = False).agg({'attended_exams':'count'}).reset_index()