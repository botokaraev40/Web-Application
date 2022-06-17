import sys

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
    return render_template('login.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
    phone_number = ''
    phone_number = request.form.get('phone-number')
    counter = 0
    symbol = 0
    format_number = ''

    if phone_number is None:
        print("Value is None")
    else:
        for i in range(0, len(phone_number)):
            if phone_number[i] == '0' or phone_number[i] == '1' or phone_number[i] == '2' or phone_number[i] == '3' or \
                    phone_number[i] == '4' or phone_number[i] == '5' or phone_number[i] == '6' or phone_number[
                i] == '7' or \
                    phone_number[i] == '8' or phone_number[i] == '9':
                counter += 1
                format_number += phone_number[i]
            elif phone_number[i] != ' ' and phone_number[i] != '(' and phone_number[i] != '(' and phone_number[
                i] != ')' and \
                    phone_number[i] != '-' and phone_number[i] != '.' and phone_number[i] != '+':
                symbol += 1
    if counter == 11 and phone_number[0] == '+' and phone_number[1] == '7':
        format_number = '8' + format_number[1:len(format_number)]

    elif counter == 11 and phone_number[0] == '8':
        format_number = format_number

    elif counter == 10:
        format_number = '8' + format_number

    return render_template('check.html', symbol=symbol, counter=counter, format_number=format_number, phone_number=phone_number)
