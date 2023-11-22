from flask import Flask, g
from flask_login import LoginManager

import models

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.secret_key = "jl;kd78jhkljkhljkhjklh56756675gjhg12gh3g"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view("login")

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close database connection after each request"""
    g.db.close()
    return response




if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
    models.initialize()
    models.User.create_user(
        name="Shahzad",
        email="shahzad@gmail.com",
        password="password",
        admin=True
    )