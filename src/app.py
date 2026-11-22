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


@app.route("/")
def index():
    """Render the front page."""
    return render_template("index.html")


@app.route("/book", methods=["GET", "POST"])
def form():
    """API request for form rendering"""

    reference_name = ""
    author = ""
    title = ""
    year = ""
    publisher = ""
    error_message = None
    if request.method == "POST":
        reference_name = request.form.get("reference_name")
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")
        publisher = request.form.get("publisher")

        try:
            year_int = int(year)
            if year_int < 1800 or year_int > 2026:
                raise ValueError

            add_book(db, reference_name, title, author, year_int, publisher)

        except ValueError:
            error_message = "Vuoden pitää olla luku väliltä 1800-2026"


    return render_template(
        "book.html",
        reference_name=reference_name,
        author=author,
        title=title,
        year=year,
        publisher=publisher,
        error=error_message,
        books=get_books())


@app.route("/inproceedings", methods=["GET", "POST"])
def inproceedings():
    """Render the conference publication form."""
    if request.method == "POST":
        pass

    return render_template("inproceeding.html")


if __name__ == '__main__':
    app.run()
