from _mysql_connector import MySQL
from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from mysql_db import Mysql
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
login_manager.login_message_category= 'warning'

app = Flask(__name__)
application = app

login_manager.init_app(app)
mysql = Mysql(app)
class User(UserMixin):
    def __init__(self, user_id, login):
        super().__init__()
        self.id = user_id
        self.login = login
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    with mysql.connection.cursor(name_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
        db_user = cursor.fetchone()
    if db_user:
        return User(user_id=db_user.id, login=db_user.login)
    return None
    for user in get_users():
        if user['user_id'] == user_id:
            return User(user_id=db_user.id, login=db_user.login)
    return None

app.config.from_pyfile('config.py')
def get_users():
    return [{'user_id': '1', 'login': 'user', 'password': 'qwerty'}]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visits')
def visits():
    if session.get('visits_count') is None:
        session['visits_count'] = 1
    else:
        session['visits_count'] += 1
    return render_template('visits.html')
@app.route('/login')
def login(db_user=None):
    if request.method == 'POST':
        login_ = request.form.get('login')
        password = request.form.get('password')
        remember_me = request.form.get('remember me') == 'on'
        with mysql.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE login=%s AND password_hash=SHA2(%s, 256);',
                           (login_, password))
            if db_user:
                login_user(User(user_id=db_user.id, login=db_user.login),
                           remember = remember_me)

        for user in get_users():
            if user['login'] == login_ and user['password'] == password:
                login_user(User(**user), remember=remember_me)
                flash("Вы успешно прошли процедуру аутентификации.", 'success')
                next_ = request.args.get('next')
                return redirect(next_ or url_for('index'))
            flash("Введены неверные логин и/или пароль.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/users')
def users():
    with mysql.connection.cursor(name_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;')
        db_user = cursor.fetchall('users/index.html', users=users)
    return render_template



@app.route('/users/new')
def new():
    return render_template('users/new.html')


@app.route('/users/<int:user_id>')
def show(user_id):
    with mysql.connection.cursor(name_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
        db_user = cursor.fetchone()
    return render_template('users/show.html', user=user)
@app.route('/users/<int:user_id>/edit')
login.required

def edit(user_id):
    with mysql.connection.cursor(name_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
        db_user = cursor.fetchone()
    return render_template('users/show.html', user=user, roles=load_roles())
