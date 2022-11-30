from .app import db


class Author (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))

class Book(db.Model ):
    id = db.Column (db.Integer, primary_key =True)
    price = db.Column(db.Float)
    title = db.Column(db.String (100))
    url = db.Column(db.String(250))
    img = db.Column(db.String(90))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    # champs books qui sera auto. renseigner dans la classe author
    author = db.relationship("Author",backref = db.backref("books", lazy="dynamic"))




def get_sample():
    return Book.query.limit(10).all()

def get_book_id(id):
    return Book.get(id)

def trie_article_moins_5e():
    return Book.query.filter(Book.price < 5.0).all()

def get_samplet():
    return Book.query.limit(100).all()

def get_author(id):
    return Author.query.filter(Author.id==id).one()