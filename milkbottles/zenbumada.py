SomeHololiveMembers = [
    {'Name': 'Tokino Sora', 'Gen': 'Gen 0', 'Debut date': '07.09.2017'}, 
    {'Name': 'Sakura Miko', 'Gen': 'Gen 0', 'Debut date': '2018.08.01 & 2018.12.25'},
    {'Name': 'Hoshimachi Suisei', 'Gen': 'Gen 0', 'Debut date': '2018.03.22 & 2019.12.01'},
    {'Name': 'Shirakami Fubuki', 'Gen': 'Gamers', 'Debut date': '2018.06.01'},
    {'Name': 'Minato Aqua', 'Gen': '2nd Gen', 'Debut date': '2018.08.08'},
    {'Name': 'Murasaki Shion', 'Gen': '2nd Gen', 'Debut date': '2018.08.17'},
    {'Name': 'Nakiri Ayame', 'Gen': '2nd Gen', 'Debut date': '2018.09.03'} ,
    {'Name': 'Oozora Subaru', 'Gen': '2nd Gen', 'Debut date': '2018.09.16'},
    {'Name': 'Ookami Mio', 'Gen': 'Gamers', 'Debut date': '2018.12.07'},
    {'Name': 'Nekomata Okayu', 'Gen': 'Gamers', 'Debut date': '2019.04.06',},
    {'Name': 'Inugami Korone', 'Gen': 'Gamers', 'Debut date': '2019.04.13',}
]

YoutubeAPIkey = 'AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU'

import pandas as pd
import csv
df = pd.read_csv('vtuber_channels.csv')

# a way to see all the files in a directory
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


# a way to convert df to csv file
# df.to_csv('holomem.csv')

from try4 import sayhi
print(sayhi())