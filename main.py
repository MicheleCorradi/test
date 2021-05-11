import sqlite3
from bottle import route, run, template, request, static_file, jinja2_view, error
import db.db_manager as d
import db.db_functions as f
import peewee


# HOMEPAGE
@route('/')
@jinja2_view('index.html')
def index():
    return {'user': 'Giulio'}


# CSS E JAVASCRIPT
@route("/static/css/<filepath:re:.*\.css>", method="GET")
def css(filepath):
    return static_file(filepath, root="static/css")

@route("/static/js/<filepath:re:.*\.js>", method="GET")
def js(filepath):
    return static_file(filepath, root="static/js")


# PARTITE
@route('/partite')
@jinja2_view('partite.html')
def select():
    # eseguire una select query per recuperare tutte le righe dalla tabella partite e visualizzarle
    return {'user': 'Giulio'}


# INSERIMENTO PARTITA
@route('/partite/insert')
@jinja2_view('partite_insert_copy.html')
def insert():
    return {'user': 'Giulio'}


# GIOCATORI
f.read(d.Giocatore)
@route('/giocatori')
def select():
    return template('giocatori.html', righe = f.rows)


# INSERIMENTO GIOCATORE
@route('/giocatori/insert', method='GET')
def insert():
    if request.GET.insert:
        # http://127.0.0.1:8080/giocatori/insert?cognome=Chiesa&insert=Inserisci
        cognome = request.GET.cognome.strip()

        db = peewee.SqliteDatabase('statistiche.db')
        db.connect()
        nuovo_giocatore = d.Giocatore(nome = cognome, totale = 0)
        nuovo_giocatore.save()
        db.close()
        
        del f.rows[:]
        f.read(d.Giocatore)

        return template('giocatori.html', righe = f.rows)
    else:        
        return template('giocatori_insert.html')


# ELIMINAZIONI GIOCATORE
@route('/giocatori/delete', method='GET')
def delete():
    if request.GET.submit:
        var = request.query.giocatore #"giocatore" è il name dell'elemento della form
        var2 = int(var)

        db = peewee.SqliteDatabase('statistiche.db')
        db.connect()
        row = d.Giocatore.get(d.Giocatore.id == var2)
        row.delete_instance()
        db.close()

        del f.rows[:]
        f.read(d.Giocatore)

        return template('giocatori.html', righe = f.rows)
    else:
        return template("giocatori_delete.html", righe = f.rows)


# ERRORE PAGINA NON TROVATA
@error(404)
def error404(error):
    return "<h1>Page not found<br>Why not start at our <a href='/'>homepage</a>?</h1>"


run(debug=True, reloader=True)
