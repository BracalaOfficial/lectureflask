from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index5.html')

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/news/pick')
def pick():
    return render_template('index.html')