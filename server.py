from flask import Flask, session, redirect, url_for, escape, request, g, Response
import psycopg2
import json

app = Flask(__name__)

def get_db():
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = psycopg2.connect(dbname="game", user="postgres", password="start")
    return g.postgres_db

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM player;")
    row = cur.fetchone()
    js = json.dumps(row)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgres_db'):
        g.postgres_db.close()