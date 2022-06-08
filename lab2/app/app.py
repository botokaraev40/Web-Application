from flask import Flask, render_template, request, url_for, make_response

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

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html'))
    if 'username' in request.cookies:
        resp.set_cookie('username', 'some name', expires=0)
    else:
        resp.set_cookie('username', 'some name')

    return resp

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/check', methods=['GET', 'POST'])
def check():

    return render_template('check.html')
