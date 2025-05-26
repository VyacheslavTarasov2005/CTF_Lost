from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "verysecretkeyplzdonthack"

@app.route('/')
def index():
    if session.get('role') == 'admin':
        with open('flag.txt') as f:
            return f"Welcome admin! Your flag is: {f.read()}"
    elif 'role' in session:
        return f"Logged in as {session['role']}"
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def login():
    session['role'] = "user"
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/<int:id>')
def find(id):
    if id == 4815162342:
        return render_template('end.html')
    if id == 815:
        return f"Don't forget to enter the numbers"
    if id == 104122:
        return f"The plane"
    else:
        return f"I love it https://www.kinopoisk.ru/series/104122/"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)