from flask import Flask, render_template, request, make_response, Response
from helpers.forms import RegisterForm
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return 'hello'

@app.route('/register', methods=['GET', 'POST'])
def login():
    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('demo.html', form=form)
    if form.validate():
        return 'success'
    return f'error: {form.errors}'
        


if __name__ == '__main__':
    app.run(debug=True)