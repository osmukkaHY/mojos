"""Main file for reference tool"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, render_template
#from flask_sqlalchemy import SQLAlchemy

from repositories.books import add_book, get_books
#from models.book import Book
from database import db, create_db


load_dotenv()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
db.init_app(app)
create_db(app)


@app.route('/', methods=["GET", "POST"])
def form():
    """API request for form rendering"""

    author = ""
    title = ""
    year = ""
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")

        print(f"Syötit kirjan: {author}, {title}, {year}")
        add_book(db, title, author, int(year))

    return render_template(
        "form.html",
        author=author,
        title=title,
        year=year,
        books=get_books())


if __name__ == '__main__':
    app.run()
