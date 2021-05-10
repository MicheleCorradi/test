import peewee
import db.db_manager

"""
CRUD operations
"""
rows = []

# Create 
def create(peewee_model):
    db = peewee.SqliteDatabase('statistiche.db')
    db.connect()

    new_row = peewee_model(nome = cognome, totale = 0)
    new_row.save()

    return db.close()

# Read OK
def read(peewee_model):
    db = peewee.SqliteDatabase('statistiche.db')
    db.connect()

    for row in peewee_model.select():
        rows.append(row)

    return db.close()

# Update
def update(peewee_model, identifier):
    db = peewee.SqliteDatabase('statistiche.db')
    db.connect()

    return db.close()

# Delete OK
def delete(peewee_model, identifier):
    db = peewee.SqliteDatabase('statistiche.db')
    db.connect()
    row = peewee_model.get(peewee_model.id == identifier)
    row.delete_instance()
    return db.close()
