from sqlalchemy import *

engine = create_engine("sqlite:///base.db")

def model_insert_user():
    req = "INSERT INTO users (user_name, user_password, user_email) VALUES( {0}, {1}, {2});".format("'bilal'","'bilal'","'bilal'")
    with engine.connect() as con:
        rs = con.execute(text(req))
        con.commit()


def model_post_user(user, password, email):
    req = "INSERT INTO users (user_name, user_password, user_email) VALUES( '{0}', '{1}', '{2}');".format(user, password, email)
    with engine.connect() as con:
        rs = con.execute(text(req))
        con.commit()