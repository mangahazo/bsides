import os
import ujson as json
import pybase64 as base64
import pysqlite3 as sqlite3
from flask import Flask, render_template, request, redirect, url_for, make_response
from utils import get_signature

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    
@app.route('/')
def index():
    if 'token' not in request.cookies:
        return redirect(url_for('login'))
    token = request.cookies['token']
    try:
        payload, signature = token.split('.')
        if signature != get_signature(payload):
            raise Exception('Invalid token')
        username = json.loads(base64.urlsafe_b64decode(payload + '==').decode()).get("username")
    except:
        return redirect(url_for('login'))
    db = get_db()
    websites = db.execute('SELECT * FROM websites WHERE user_id = (SELECT id FROM users WHERE username = ?)', (username,)).fetchall()
    return render_template('index.html', websites=websites)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        if user:
            payload = json.dumps({'username': username}).encode()
            payload = base64.urlsafe_b64encode(payload).decode().rstrip('=')
            signature = get_signature(payload)
            token = "{}.{}".format(payload, signature)
            response = make_response(redirect(url_for('index')))
            response.set_cookie('token', token)
            return response
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if user:
            return render_template('register.html', error='Username already exists')
        else:
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            return redirect(url_for('login'))
    else:
        return render_template('register.html')
    
@app.route('/create_website', methods=['GET', 'POST'])
def create_website():
    if request.method == 'POST':
        token = request.cookies['token']
        try:
            payload, signature = token.split('.')
            if signature != get_signature(payload):
                raise Exception('Invalid token')
            username = json.loads(base64.urlsafe_b64decode(payload + '==').decode()).get("username")
        except:
            return redirect(url_for('login'))
        content = request.form.get('content', '')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        website_id = os.urandom(16).hex()
        db.execute('INSERT INTO websites (id, content, user_id) VALUES (?, ?, ?)', (website_id, content, user['id']))
        db.commit()
        return redirect(f"/website/{website_id}")
    else:
        return render_template('create_website.html')
    
@app.route('/website/<website_id>')
def view_website(website_id):
    db = get_db()
    website = db.execute('SELECT * FROM websites WHERE id = ?', (website_id,)).fetchone()
    if not website:
        return 'Not found', 404
    else:
        return render_template('view_website.html', website=website)
    

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=os.name == 'nt')