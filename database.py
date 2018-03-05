import psycopg2

conn = psycopg2.connect(dbname="game", user="postgres", password="start")
cur = conn.cursor()
cur.execute("SELECT * FROM player;")
row = cur.fetchone()
print(row)
cur.close()
conn.close()
