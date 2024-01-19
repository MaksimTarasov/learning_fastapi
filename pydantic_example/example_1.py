"""
В даннном модул приведены примеры работы с библиотекой pydantic

Самый основной способ определения схем в Pydantic это модели.
Модели это простой класс который наследуется от pydentic.BaseModel и определнение полей
как аннотированые атрибуты. Есть много схожего с датаклассами Python. Непроверенные данные
подаются в модель и после парсинга и валидации данные будут гарантиролваннно соответствоватттть
полям и типам данных указнных в модели.
"""

from pydantic import BaseModel, Field, ValidationError
from typing import List

"""
    Простая модель для валидации
"""


class GroundBait(BaseModel):
    id: int
    component: str


dj = {
    "id": "1",
    "component": "sensas"
}
try:
    gb = GroundBait(**dj)
except ValidationError as e:
    print(e)
else:
    # Вывод в виде json
    print(gb.model_dump_json(indent=2))

"""
 Задание дефолтных значений для полей
"""


class Beer(BaseModel):
    # Задаем дефлотные значения полей
    liters: int = Field(default=1)
    name: str = Field(default='Ostmark')


holsten = {"liters": 2, "name": "Holsten"}
try:
    beer = Beer()
# Если выскачит исклюечение то оно обработается и выведется в читабельном виде
except ValidationError as e:
    print(e)
else:
    print(beer)

"""
    Условия в значениях полей
    gt=40 означает, что занчение поля должно быть не меенее 40
"""


class Feeder(BaseModel):
    form: str = Field(default='bullet')
    mass: int = Field(gt=40)


fd = {"form": 'bullet', "mass": 40}
try:
    feeder = Feeder(**fd)
except ValidationError as e:
    print(e)
else:
    print(feeder)
