from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import text
from model import * 

app = Flask(__name__)
engine = create_engine("sqlite:///base.db")

#metadata_obj = MetaData(schema="main")
#metadata_obj.reflect(bind=engine)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/user/')
def get_user():
    with engine.connect() as con:
        rs = con.execute(text('SELECT * FROM users'))
        user_id = []
        for row in rs:
            user_id.append(row)
    return render_template('user.html', tmpl=user_id)


@app.route('/user/insert/')
def insert_user():
    model_insert_user()
    return redirect(url_for('get_user'))


@app.route('/user/post/', methods=['GET','POST'])
def post_user():
    user = ''
    password = ''
    email = ''
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        email = request.form['email']
    model_post_user(user, password, email)
    return render_template('user_add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)