from pydantic import BaseModel, ValidationError, Field
from typing import List
"""
Простая модель для валидации 
"""
class GroundBait(BaseModel):
    id: int
    component: str

dj = {
    """В модели указан тип int, ели мы число указали в виде строки
       то оно преобразуется в число. Если будет текст, то выйдет исключение  
    """
    "id": "1",
    "component": "sensas"
}
try:
    gb = GroundBait(**dj)
except ValidationError as e:
    print(e)
else:
    #Вывод в виде json
    print(gb.model_dump_json(indent=2))


