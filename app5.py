from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Hello, Bracala"
    return render_template('index2.html', headline=headline)