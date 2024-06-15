SomeHololiveMembers = [
    {'Name': 'Tokino Sora', 'Gen': 'Gen 0', 'Debut date': '07.09.2017'}, 
    {'Name': 'Sakura Miko', 'Gen': 'Gen 0', 'Debut date': '2018.08.01 & 2018.12.25'},
    {'Name': 'Hoshimachi Suisei', 'Gen': 'Gen 0', 'Debut date': '2018.03.22 & 2019.12.01'},
    {'Name': 'Shirakami Fubuki', 'Gen': 'Gamers & 1st Gen', 'Debut date': '2018.06.01'},
    {'Name': 'Minato Aqua', 'Gen': '2nd Gen', 'Debut date': '2018.08.08'},
    {'Name': 'Murasaki Shion', 'Gen': '2nd Gen', 'Debut date': '2018.08.17'},
    {'Name': 'Nakiri Ayame', 'Gen': '2nd Gen', 'Debut date': '2018.09.03'} ,
    {'Name': 'Oozora Subaru', 'Gen': '2nd Gen', 'Debut date': '2018.09.16'},
    {'Name': 'Ookami Mio', 'Gen': 'Gamers', 'Debut date': '2018.12.07'},
    {'Name': 'Nekomata Okayu', 'Gen': 'Gamers', 'Debut date': '2019.04.06',},
    {'Name': 'Inugami Korone', 'Gen': 'Gamers', 'Debut date': '2019.04.13',}
]
import csv
with open('some_members_.csv', 'wt', newline='') as f:
    fieldnames = SomeHololiveMembers[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in SomeHololiveMembers:
        writer.writerow(w)

with open('some_members_.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        