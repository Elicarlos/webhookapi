from peewee import *

import datetime
from playhouse.postgres_ext import *

# db = PostgresqlDatabase(
#     database='',
#     host='', 
#     user='', 
#     password=''

# )

# db = SqliteDatabase('my_database.db')

db = SqliteDatabase('my_database.db')

class BaseModel(Model):    
    created_at = DateTimeField(default=datetime.datetime.now)   
    class Meta:
        database = db

class User(BaseModel):
    pass

class LogCliente(BaseModel):
    nome = CharField(max_length=50, null=True) 
    email = CharField(max_length=100, null=True)
    status = CharField(max_length=50, null=True)
    valor = DecimalField(max_digits=1000, decimal_places=2,null=True)
    forma_pagamento = CharField(max_length=50, null=True)  
    parcelas = IntegerField(null=True)

    def insira_varios(dados):
        with db.atomic() as transaction:  # Opens new transaction.
            try:
                LogCliente.insert_many(dados).execute()
            except Exception as e:
                # Because this block of code is wrapped with "atomic", a
                # new transaction will begin automatically after the call
                # to rollback().
                transaction.rollback()
                print(e)
                error_saving = True

            # create_report(error_saving=error_saving)
            # Note: no need to call commit. Since this marks the end of the
            # wrapped block of code, the `atomic` context manager will
            # automatically call commit for us.



db.connect()
def create_tables():
    db.create_tables([
        LogCliente,
        User
    ])

create_tables()