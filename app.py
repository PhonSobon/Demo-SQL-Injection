# from flask import Flask, request, g
# import sqlite3

# app = Flask(__name__)
# DATABASE = 'demo.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

# @app.route('/')
# def index():
#     return '''
#         <form action="/login" method="post">
#             Username: <input type="text" name="username"><br>
#             Password: <input type="password" name="password"><br>
#             <input type="submit" value="Login">
#         </form>
#     '''

# # @app.route('/login', methods=['POST'])
# # def login():
# #     username = request.form['username']
# #     password = request.form['password']
# #     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
# #     user = query_db(query, one=True)
    
# #     if user:
# #         return f"Welcome {username}!"
# #     else:
# #         return "Login failed"

# # if __name__ == '__main__':
# #     app.run(debug=True)
    
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#     user = query_db(query, one=True)
    
#     if user:
#         return f"Welcome {username}!"
#     else:
#         return "Login failed"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, g, render_template, send_from_directory
import sqlite3

app = Flask(__name__)
DATABASE = 'demo.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    user = query_db(query, one=True)
    
    if user:
        return f"Welcome {username}!"
    else:
        return render_template('login.html', error="Login failed")

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
