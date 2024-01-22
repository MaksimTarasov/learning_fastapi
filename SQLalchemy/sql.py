"""
В данном разделе изучим SQL alchemy)))
"""
from sqlalchemy import create_engine, text, MetaData

#Использование SQLalchemy CORE
engine = create_engine("sqlite+pysqlite:///test.db", echo=True)
#Создание движка), Echo=true включает режим логирования и вводит на экран логи транзакции
with engine.connect() as con:
    #Чтение данных из базв
    result = con.execute(text('select * from Beer'))
    #print(result.all())
    for i in result:
        print(i.name)


