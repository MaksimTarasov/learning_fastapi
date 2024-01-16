"""
Простейшее приложение FastAPI
"""
from fastapi import FastAPI

app = FastAPI()
"""
Тестовая модель базы данных
"""
db = {1: {'name': 'Ivar', 'age': 30},
      2: {'name': 'Bjorn', 'age': 40},
      3: {'name': 'Ragnar', 'age': 50},
      }

@app.get("/")
def read_root():
    """
    Функция фозвращающая ответ за запрос GET, endpoint "/"
    :return:
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {"Viking": db.get(item_id, 'Null')}

@app.get("/age")
def read_age(name: str = ''):
    if name:
        for i in db.keys():
            if db[i]['name'] == name:
                return f"{name}, age {db[i]['age']}"
        return f"{name} не найден."
    return [db[key]['name'] for key in db.keys()]

@app.post("/add")
def add_viking(name: str, age: int):
    ids = list(db.keys())
    ids.sort()
    id = ids[-1] + 1
    db[id] = {'name': name, 'age': age}
    return {"Status OK: 200": db[id]}

#uvicorn main:app --reload