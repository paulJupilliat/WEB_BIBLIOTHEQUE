from .models import Author, Book
import yaml
import yaml
import os.path
import click
from .app import app, db


# Books = yaml.safe_load(open(os.path.join(os.path.dirname(__file__),"data.yml")))


# # Pour avoir un id
# i = 0
# for book in Books:
#     book['id'] = i
#     i += 1


@app.cli.command()
def syncdb():
    '''
    Création de toute les tables de la bd
    '''
    db.create_all()

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''Creates the tables and populates them with data. '''
    # création de toutes les tables
    db. create_all()
    # chargement de notre jeu de données
    books = yaml.load(open(filename))
    # import des modèles
    # première passe : création de tous les auteurs
    authors = {}
    for b in books:
        a = b["author"]
        if a not in authors:
            o = Author(name=a)
            db.session.add(o)
            authors[a] = o
    db.session.commit()
    # deuxième passe : création de tous les livres
    for b in books:
        a = authors[b["author"]]
        o = Book(price=b["price"],
            title=b["title"],
            url=b["url"],
            img=b["img"],
            author_id=a.id)
        db.session.add(o)
    db.session.commit()
