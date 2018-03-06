from flask import Flask, session, redirect, url_for, escape, request, g, Response, abort, make_response
import psycopg2
import json
import os, base64, uuid


class User:
    def __init__(self,username, password):
        pass

users={}
app = Flask(__name__)
def get_db():
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = psycopg2.connect(dbname="game", user="postgres", password="start")
    return g.postgres_db
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        cur = db.cursor()
        username = request.form['username']
        password = request.form['password']
        cur.execute("SELECT id, name, sessionid FROM users where name = %s and password = %s;",(username,password,))
        row = cur.fetchone()
    
        if row:
            sessionid = str(uuid.uuid4())
            cur.execute("update users set sessionid = %s where name = %s;",(sessionid,username,))
            cur.close()
            db.commit()
            js = json.dumps({"sessionid":sessionid})
            resp = Response(js, status=200, mimetype='application/json')
            resp.set_cookie(key='GAMESID',value=sessionid)
            return resp
        else:
            abort(401)
            return
    return
@app.route('/game/request', methods=['POST'])
def request_game():
    #check for open game
    #if open respose player session
    #else
    #create new game and response player session
    pass
@app.route('/game/commit', methods=['POST'])
def commit_game():
    #check for open commit
    #set start camp select
    #wait for last commit
    #respose game session
    pass
@app.route('/game/lockedin', methods=['POST'])
def lockedin_game():
    #set player locked in
    #response start code
    pass
@app.route('/game/ready', methods=['GET'])
def ready_game():
    #respose gamedata
    pass
@app.route('/game/client_ready', methods=['GET'])
def client_ready():
    #if all player ready
    #start game
    #else
    #respose wait
    pass
@app.route('/player/command', methods=['POST'])
def player_command():
    #set new command
    #response new pos
    pass
@app.route('/player/ping', methods=['POST'])
def player_ping():
    #set new command
    #response new pos
    pass
@app.route('/user/<username>')
def show_user_profile(username):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users where name = %s;",(username,))
    row = cur.fetchone()
    cur.close()
    js = json.dumps(row)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgres_db'):
        g.postgres_db.close()