import datetime
from peewee import *

# db = PostgresqlDatabase(
#     database='',
#     host='', 
#     user='', 
#     password=''

# )

# db = SqliteDatabase('my_database.db')

db = SqliteDatabase('my_database.db')

class Cliente():
    "nome": "Archana",
  "email": "Nala2006@express.ngo",
  "status": "aprovado",
  "valor": 858,
  "forma_pagamento": "pix",
  "parcelas": 5


db.connect()
def create_tables():
    db.create_tables([
        tb, 
        tb,
        

    ])