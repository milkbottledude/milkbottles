SomeHololiveMembers = [
    {'Name': 'Tokino Sora', 'Gen': 'Gen 0', 'Debuted': 2017}, 
    {'Name': 'Sakura Miko', 'Gen': 'Gen 0', 'Debuted': 2018},
    {'Name': 'Hoshimachi Suisei', 'Gen': 'Gen 0', 'Debuted': 2019},
    {'Name': 'Shirakami Fubuki', 'Gen': 'Gamers & 1st Gen', 'Debuted': 2018},
    {'Name': 'Minato Aqua', 'Gen': '2nd Gen', 'Debuted': 2018},
    {'Name': 'Murasaki Shion', 'Gen': '2nd Gen', 'Debuted': 2018},
    {'Name': 'Nakiri Ayame', 'Gen': '2nd Gen', 'Debuted': 2018} ,
    {'Name': 'Oozora Subaru', 'Gen': '2nd Gen', 'Debuted': 2018},
    {'Name': 'Ookami Mio', 'Gen': 'Gamers', 'Debuted': 2018},
    {'Name': 'Nekomata Okayu', 'Gen': 'Gamers', 'Debuted': 2019},
    {'Name': 'Inugami Korone', 'Gen': 'Gamers', 'Debuted': 2019}
]
import json

#with open('some_members_.json', 'w') as f:
    #json.dump(SomeHololiveMembers, f)

#print(open('some_members_.json').read())

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, Enum
engine = create_engine(\
    'sqlite:///sukoshi(json version).db', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Ichi(Base):
    __tablename__ = 'sukoshi'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Gen = Column(String)
    Debuted = Column(Integer)

    def __repr__(self):
        return "<Ichi(Name='%s', Gen='%s', Debuted='%s')>"\
            %(self.Name, self.Gen, self.Debuted)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

#Adding and expunging a single instance from the session
# Sora_chan = Ichi(**SomeHololiveMembers[0])
# session.add(Sora_chan)
# print(session.new)

# session.expunge(Sora_chan)
# print(session.new)

#Adding all instances to session and committing them to database
Ichi_rows = [Ichi(**m) for m in SomeHololiveMembers]
session.add_all(Ichi_rows)
session.commit

print(session.query(Ichi).count())
result = session.query(Ichi).filter_by(Gen='2nd Gen')
for m in list(result):
    print(m)