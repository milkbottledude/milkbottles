import pandas as pd
from zenbumada import SomeHololiveMembers
df = pd.DataFrame(SomeHololiveMembers)
# df = df.T
# print(df.iloc[0]) is the same as print(df['Name']) in this case for this dataframe
df['Cute?'] = True
df['Pon?'] = "sa"
df['No. of Livestreams'] = True
df['Channel id'] = 'Aru'

def edit_value(Name, column, new_value):
    df.loc[df['Name'] == Name, column] = new_value

def user_edit():
    name = str.title(input('Name: '))
    column = str.title(input('Column: '))
    new_value = input('New value: ')
    df.loc[df['Name'] == name, column] = new_value
    return df


df.loc[df['Name'] == 'Sakura Miko', 'Pon?'] = 'hai'
df.loc[df['Name'] == 'Minato Aqua', 'Pon?'] = 'hai'

edit_value('Sakura Miko', 'Channel id', 'UC-hM6YJuNYVAmUWxeIr9FeA')
edit_value('Tokino Sora', 'Channel id', 'UCp6993wxpyDPHUpavwDFqgg')
edit_value('Hoshimachi Suisei', 'Channel id', 'UC5CwaMl1eIgY8h02uZw7u8A')
edit_value('Shirakami Fubuki', 'Channel id', 'UCdn5BQ06XqgXoAxIhbqw5Rg')
edit_value('Minato Aqua', 'Channel id', 'UC1opHUrw8rvnsadT-iGp7Cg')
edit_value('Murasaki Shion', 'Channel id', 'UCXTpFs_3PqI41qX2d9tL2Rw')
edit_value('Nakiri Ayame', 'Channel id', 'UC7fk0CB07ly8oSl0aqKkqFg')
edit_value('Oozora Subaru', 'Channel id', 'UCvzGlP9oQwU--Y0r9id_jnA')
edit_value('Ookami Mio', 'Channel id', 'UCp-5t9SrOQwXMU7iIjQfARg')
edit_value('Nekomata Okayu', 'Channel id', 'UCvaTdHTWBGv3MKj3KVqJVCw')
edit_value('Inugami Korone', 'Channel id', 'UChAnqc_AY5_I3Px5dig3X1Q')
edit_value('Sakura Miko', 'Debut date', '2018.12.25')
edit_value('Hoshimachi Suisei', 'Debut date', '2019.12.01')

df.replace({True:'Aru'})

print(df)

