from flask import Flask, render_template, request, url_for

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/args')
def args():
    return render_template('args.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')