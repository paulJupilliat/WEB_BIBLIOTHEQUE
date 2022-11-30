from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from .app import app, db
from flask import render_template , url_for, redirect
from .models import get_sample, trie_article_moins_5e, get_samplet, get_author, Author

@app.route ("/")

def home ():
    return render_template ("home.html", 
        title =" My Books", 
        books = get_sample())

@app.route("/detail/<id>")
def detail(id):
    books = get_samplet()
    book = books[int(id)-1]
    
    return render_template("detail.html",book=book)

@app.route("/home/trie")
def trie():
    return render_template("trie.html",
    title = "-5$",
    books = trie_article_moins_5e())
    #pourquoi il m'affiche les livre au dessus de 10 mais ne veux pas que je regarde ces details


class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template("edit-author.html", author=a, form=f)


# -----------------------------------------------------------------
@app.route("/save/author/", methods =("POST",))
def save_author():
    a =None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('detail', id=a.id))
    a = get_author(int(f.id.data))
    return render_template("edit-author.html", author=a, form=f)