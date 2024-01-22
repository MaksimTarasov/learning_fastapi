"""
Пример для понимания работы с метадаными
"""


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

edgien = create_engine("sqlite+pysqlite:///test.db", echo=True)
metadata = MetaData()
#Опреление таблицы
beer_table = Table(
#Имя таблицы
    "Beer",
 #метаданны таблицы
    metadata,
    #Определение колонок таблицa
    Column("id", Integer),
    Column("name", String),
    Column("volume", Integer)
)
vodka_table = Table(
    "Vodka",
    metadata,
    Column("id", Integer),
    Column("name", String),
    Column("value", Integer)
)
metadata.create_all(edgien)
print(metadata.tables)
print(beer_table.c.name)
sel = beer_table.select()
print(sel)
sel = select(beer_table.c.name)
print(sel)
with edgien.connect() as con:
    res = con.execute(sel)
    print(res.all())
    con.commit()