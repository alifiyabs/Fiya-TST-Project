from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import uvicorn
import models

app = FastAPI()

def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    return models.Base.metadata.create_all(bind=engine)

#Buat API untuk create user
@app.post('/user')
def createUser(userReq: schemas.User, db: Session = Depends(getDatabase)):
    new_user = models.User(username=userReq.username, password = userReq.password, email = userReq.email)
    db.add(new_user)
    db.commit()


@app.get('/user')
def getUser():
    pass

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)