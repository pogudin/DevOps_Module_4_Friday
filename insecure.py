from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')  # User input
    conn = sqlite3.connect('db.sqlite')
    # SQL injection - user input in query
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor = conn.execute(query)  # CodeQL flags this!
    return str(cursor.fetchone())
