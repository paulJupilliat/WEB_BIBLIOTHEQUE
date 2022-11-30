from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy 
import os.path


app = Flask ( __name__ )
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

def mkpath (p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__),p))

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+ mkpath('../books.db'))
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "26566be2-bdb3-4e04-bab6-b98ec3e751f3"
db = SQLAlchemy(app)