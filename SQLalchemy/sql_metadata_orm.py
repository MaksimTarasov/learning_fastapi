"""
пример сздания метаданны через ORM
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import registry, declarative_base

engien = create_engine("sqlite+pysqlite:///test.db", echo=True)

#1 вариант создания базового класса
#Содание реестра для метаданных
meta_reg = registry()
#Создание базового класса
Base = meta_reg.generate_base()
#Создание таблицы
class JuseTable(Base):
    __tablename__ = "Juse"
    id = Column(Integer, primary_key=True)
    name= Column(String)
    volume = Column(Integer)
meta_reg.metadata.create_all(engien)

#2 Вариант
#Создание реестра метаданных и базового класса
Base2 = declarative_base()

class Water(Base2):
#Создание таблицы
    __tablename__ = "Water"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    volume = Column(Integer)
#Создаюм таблицу в БД,
Base2.metadata.create_all(engien)