from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

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
    return render_template('catalog.html', color='green')


if __name__ == '__main__':
    app.run(debug=True)
