import requests
from flask import Flask, redirect, url_for, render_template, jsonify
from flask import request, session

from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
@app.route('/home')
def hello_func():
    found = False
    if found:
        name = 'Nitzan Agam'
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')


@app.route('/catalogs')
def catalogs_func():
    return redirect('/catalog')


@app.route('/about')  # this is another page
def about_func():
    return render_template('about.html',
                           uni='BGU',
                           profile={'First Name': 'Nitzan',
                                    'Last Name': 'Agam'},
                           degrees=['BSc', 'MSc'],
                           hobbies=('dancing',
                                    'art',
                                    'reading',
                                    'surfing'))


@app.route('/catalog')
def catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html',p_name=product,p_size=size, color='green')
    return render_template('catalog.html')


@app.route('/login',methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # DB
        session.username = request.form['username']
        session.password = request.form['password']
        return render_template('index.html', username=session.username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    session['LoggedIn'] = False
    return render_template('index.html')


@app.route('/assignment8')
def hobbies_func():
    currentUser = 'Nitzan'
    return render_template('assignment8.html',
                           name=currentUser,
                           travel={'New York', 'Bangkok', 'London', 'Barcelona'},
                           Dancing={'Folklore', 'Jazz', 'Mainstream'},
                           bShows={'Mama Mia', 'Frozen', 'Kinky Boots'})


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    MyUsers = [
        {'id': 1, 'email': "nitzan.agam@gmail.in", 'firstname': "Nitzan", 'lastname': "Agam"},
        {'id': 2, 'email': "kimkardash@gmail.in", 'firstname': "Kim", 'lastname': "Kardashian"},
        {'id': 3, 'email': "Khloe.kardash@gmail.in", 'firstname': "Khloe", 'lastname': "Kardashian"},
        {'id': 4, 'email': "Kortney.kardash@gmail.in", 'firstname': "Kortney", 'lastname': "Kardashian"},
        {'id': 5, 'email': "kylie.jenner@gmail.in", 'firstname': "Kylie", 'lastname': "Kardashian"},
        {'id': 6, 'email': "kendel.jenner@gmail.in", 'firstname': "Kendel", 'lastname': "Kardashian"}
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    elif request.method == 'POST':
        if 'username' in request.form:
            username = request.form['username']
            session['LoggedIn'] = True
            session['username'] = username
        else:
            session['LoggedIn'] = False
            session['username'] = ''
            username = ''
    return render_template('Assignment9.html',
                           MyUsers=MyUsers,
                           username=username,
                           firstname=firstname,
                           request_method=request.method)


# assignment 10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


# assignment 11
@app.route('/assignment11')
def assignment11_fun():
    return render_template('assignment11.html')


@app.route('/assignment11/users')
def assignment11_users_fun():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.id}'] = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
    return jsonify(return_dict)


@app.route('/assignment11/outer_source')
def assignment11_outer_source_fun():
    return render_template('request_outer_source.html')


def get_user(id):
    if (id != ""):
        user_id = int(id)
        return requests.get(f'https://reqres.in/api/users/{user_id}').json()

    users = []
    length = len(requests.get(f'https://reqres.in/api/users').json()['data'])

    for i in range(1, length+1):
        res = requests.get(f'https://reqres.in/api/users/{i}')
        res = res.json()
        users.append(res)
    return users


@app.route('/req_backend')
def req_backend():
    if "user_id" in request.args:
        user_id = request.args['user_id']
        if user_id == "":
            users = get_user(user_id)
            return render_template('request_outer_source.html', users=users)
        else:
            user = get_user(user_id)
            return render_template('request_outer_source.html', user=user)

    return render_template('request_outer_source.html')

## assignment 12
@app.route('/assignment12')
def assignment12_func():
    return render_template("assignment12.html")


@app.route('/assignment12/restapi_users', defaults={'user_id': -1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_user_func(user_id):
    if user_id == -1:
        return_dict = {}
        query = 'select * from users;'
        users = interact_db(query=query, query_type='fetch')
        for user in users:
            return_dict[f'user_{user.id}'] = {
                'id': user.id,
                'first name': user.first_name,
                'last name': user.last_name,
                'email': user.email,
            }
    else:
        query = 'select * from users where id=%s;' % user_id
        users = interact_db(query=query, query_type='fetch')
        if len(users) == 0:
            return_dict = {
                'status': 'failed',
                'message': 'user not found'
            }
        else:
            return_dict = {
                'status': 'success',
                'id': users[0].id,
                'first_name': users[0].first_name,
                'last_name': users[0].last_name,
                'email': users[0].email,
            }

    return jsonify(return_dict)

if __name__ == '__main__':
    app.run(debug=True)

