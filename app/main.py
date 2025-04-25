from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", status_code=201)
def create_user(user: User):
    users.append(user)
    return {"message": "Usuario creado", "user": user}
