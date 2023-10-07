import pandas as pd

path = './DataSet/survey_results_public.csv'

data = pd.read_csv(path)

val = data['Hobbyist'].value_counts()

l = dict(val)
print(l['Yes'])
