from flask import Flask, redirect, url_for, render_template
from flask import request, session

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
    return render_template('index.html')


@app.route('/assignment8')
def hobbies_func():
    currentUser = 'Nitzan'
    return render_template('assignment8.html',
                           name=currentUser,
                           travel={'New York', 'Bangkok', 'London', 'Barcelona'},
                           Dancing={'Folklore', 'Jazz', 'Mainstream'},
                           bShows={'Mama Mia', 'Frozen', 'Kinky Boots'})


if __name__ == '__main__':
    app.run(debug=True)

