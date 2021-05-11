import peewee

db = peewee.SqliteDatabase('statistiche.db')

class Partita(peewee.Model):
    squadra_casa = peewee.CharField()
    squadra_fuoricasa = peewee.CharField()
    risultato = peewee.CharField()
    marcatori = peewee.TextField()
    class Meta:
        database = db
        db_table = 'partite'


class Giocatore(peewee.Model):
    nome = peewee.CharField()
    totale = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'giocatori' 


db.connect()

db.create_tables([Partita, Giocatore])


