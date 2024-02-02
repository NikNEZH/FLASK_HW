from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)
        return resp

    return render_template('index.html')


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    return render_template('welcome.html', name=name)


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp


if __name__ == '__main__':
    app.run()