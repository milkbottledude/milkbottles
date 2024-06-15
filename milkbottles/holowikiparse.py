import pandas as pd
table = pd.read_html("https://hololive.wiki/wiki/Members")
df = pd.DataFrame(table[0])
del df['Unnamed: 0'], df['Notes']
listf =[]
for i in range(86):
    if 'HOLOSTARS' in df.at[i, 'Generation']:
        continue
    else:
        listf.append(df.iloc[i])
newdf = pd.DataFrame(listf)
print(newdf)

from df_to_gsheet import df_to_gsheet_func
df_to_gsheet_func(1, newdf)