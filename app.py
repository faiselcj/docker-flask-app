from flask import Flask
import os
import psycopg2
import redis

app = Flask(__name__)
r = redis.Redis(host='cache', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('hits')
    return f"Hello! Visit count: {count}, ENV={os.getenv('APP_ENV')}"

@app.route('/db')
def db_check():
    conn = psycopg2.connect(
        host="db", dbname="appdb", user="postgres", password="pass"
    )
    return "DB Connected!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
