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

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
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

# from here is: https://www.educative.io/answers/how-to-create-a-table-in-sqlalchemy
Base.metadata.create_all(engine)

# Print the names of all tables in the database
def print_all_tables(engine):
    # To load metdata and existing database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    tables = metadata.tables.keys()
    
    print("List of tables:")
    for table in tables:
        print(table)

# Print all tables in the in-memory database
print_all_tables(engine)
