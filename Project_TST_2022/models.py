from sqlalchemy import Column, Integer, String

# Buat tabel, tapi karena kita di python kita buatnya class
from database import Base

class User(Base):
    #Ini kalian buat tabel, terus kolomnya ada ID dan name
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)