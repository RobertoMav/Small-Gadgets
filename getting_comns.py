import pandas as pd

## Set path to file "submissions.csv"
PATH = ""

df_sub = pd.read_csv(PATH)

print(df_sub.columns)

