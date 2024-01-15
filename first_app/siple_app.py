
from fastapi import FastAPI

app = FastAPI()
db = {1: {'name': 'Ivar', 'age': 30},
      2: {'name': 'Bjorn', 'age': 40},
      3: {'name': 'Ragnar', 'age': 50},
      }
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {"Viking": db.get(item_id, 'Null'),}
@app.get("/age")
def read_age(name: str = ''):
    if name:
        for i in db.keys():
            if db[i]['name'] == name:
                return f"{name}, age {db[i]['age']}"
        return f"{name} не найден."
    return [db[key]['name'] for key in db.keys()]

#uvicorn main:app --reload