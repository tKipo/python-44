from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('sqlite:///University.db', echo=True)
conn = engine.connect()
meta = MetaData()

university = Table(
    'university', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('addr', String)
)

faculty = Table(
    'faculty', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('id_un', Integer)
)

speciality = Table(
    'speciality', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('id_fac', Integer)
)

subject = Table(
    'subject', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('id_spec', Integer)
)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
    Column('id_spec', Integer),
)

meta.create_all(engine)

# conn.execute(university.insert(), [
#     {'id': 1, 'name': 'BSUIR', 'addr': 'Minsk, P. Brovki st., 6'},
#     {'id': 2, 'name': 'BSU', 'addr': 'Minsk, Independence av., 4'},
#     {'id': 3, 'name': 'BNTU', 'addr': 'Minsk, Independence av., 65'},
# ])
#
# conn.execute(faculty.insert(), [
#     {'id': 1, 'name': 'IE', 'id_un': 1},
#     {'id': 2, 'name': 'IIP', 'id_un': 1},
#     {'id': 3, 'name': 'HIM', 'id_un': 2},
#     {'id': 4, 'name': 'AVTOM', 'id_un': 2},
#     {'id': 5, 'name': 'AVTOTR', 'id_un': 3},
#     {'id': 6, 'name': 'KOMPTEH', 'id_un': 3},
# ])
#
# conn.execute(speciality.insert(), [
#     {'id': 1, 'name': 'EIOP', 'id_fac': 1},
#     {'id': 2, 'name': 'KSIS', 'id_fac': 2},
#     {'id': 3, 'name': 'FH', 'id_fac': 3},
#     {'id': 4, 'name': 'AVTOMSIS', 'id_fac': 4},
#     {'id': 5, 'name': 'PO', 'id_fac': 5},
#     {'id': 6, 'name': 'II', 'id_fac': 6},
# ])
#
# conn.execute(subject.insert(), [
#     {'id': 1, 'name': 'OrgTrud', 'id_spec': 1},
#     {'id': 2, 'name': 'Progr', 'id_spec': 2},
#     {'id': 3, 'name': 'OrgHim', 'id_spec': 3},
#     {'id': 4, 'name': 'Seti', 'id_spec': 4},
#     {'id': 5, 'name': 'OS', 'id_spec': 5},
#     {'id': 6, 'name': 'Python', 'id_spec': 6},
# ])
#
# conn.execute(students.insert(), [
#     {'id': 1, 'name': 'Vasiliy', 'lastname': 'Pupkin', 'id_spec': 1},
#     {'id': 2, 'name': 'Nikolay', 'lastname': 'Belich', 'id_spec': 1},
#     {'id': 3, 'name': 'Maria', 'lastname': 'Petrova', 'id_spec': 1},
#     {'id': 4, 'name': 'Sergey', 'lastname': 'Zhabo', 'id_spec': 2},
#     {'id': 5, 'name': 'Kiryl', 'lastname': 'Batonov', 'id_spec': 2},
#     {'id': 6, 'name': 'Maria', 'lastname': 'Magdalena', 'id_spec': 2},
#     {'id': 7, 'name': 'Irina', 'lastname': 'Sopanaru', 'id_spec': 3},
#     {'id': 8, 'name': 'Niko', 'lastname': 'Niners', 'id_spec': 3},
#     {'id': 9, 'name': 'Joey', 'lastname': 'Jordison', 'id_spec': 3},
#     {'id': 10, 'name': 'Mike', 'lastname': 'Gordon', 'id_spec': 4},
#     {'id': 11, 'name': 'Anastsiya', 'lastname': 'Starova', 'id_spec': 4},
#     {'id': 12, 'name': 'Viktor', 'lastname': 'Lukashin', 'id_spec': 4},
#     {'id': 13, 'name': 'Boris', 'lastname': 'Greben', 'id_spec': 5},
#     {'id': 14, 'name': 'Vlad', 'lastname': 'Stupin', 'id_spec': 5},
#     {'id': 15, 'name': 'Sergey', 'lastname': 'Barmaley', 'id_spec': 5},
#     {'id': 16, 'name': 'Vadim', 'lastname': 'Trusov', 'id_spec': 6},
#     {'id': 17, 'name': 'Valeriy', 'lastname': 'Kipelov', 'id_spec': 6},
# ])

j = students.join(speciality, students.c.id_spec == speciality.c.id)
stmt = select([students, speciality]).select_from(j).where(speciality.c.name == 'KSIS')
print(stmt)
result = conn.execute(stmt)
for row in result:
    print(row)

#или можно вывести по индексу специальности
# s = students.select().where(students.c.id_spec == 2)
# result = conn.execute(s)
# for row in result:
#     print(row)
