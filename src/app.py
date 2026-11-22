"""Main file for reference tool"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, abort
# from flask_sqlalchemy import SQLAlchemy

from repositories.books import add_book, get_books, get_book, delete_book, edit_book
# from models.book import Book
from repositories.articles import add_article, get_articles, delete_article
# from models.article import Article
from repositories.inproceedings import add_inproceedings, get_inproceedings, delete_inproceedings
# from models.inproceedings import Inproceedings
from database import db, create_db
from validators import parse_year


load_dotenv()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
create_db(app)


@app.route("/")
def index():
    """Render the front page."""
    return render_template(
        "index.html",
        books=get_books(),
        articles=get_articles(),
        inproceedings=get_inproceedings()
    )


@app.route("/book", methods=["GET", "POST"])
def book():
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
            year_int = parse_year(year)
        except ValueError as err:
            error_message = str(err)

        else:
            add_book(db, reference_name, title, author, year_int, publisher)

    return render_template(
        "book.html",
        reference_name=reference_name,
        author=author,
        title=title,
        year=year,
        publisher=publisher,
        error=error_message,
        books=get_books(),
        is_edit=False
    )


@app.route("/inproceedings", methods=["GET", "POST"])
def inproceedings():
    """Render the conference publication form."""
    reference_name = ""
    author = ""
    title = ""
    year = ""
    series = ""
    pages = ""
    error_message = None

    if request.method == "POST":
        reference_name = request.form.get("reference_name")
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")
        series = request.form.get("series", "")
        pages = request.form.get("pages", "")

        try:
            year_int = parse_year(year)
        except ValueError as err:
            error_message = str(err)
        else:
            add_inproceedings(
                db, reference_name, title, author, year_int, series, pages
            )

    return render_template(
        "inproceeding.html",
        reference_name=reference_name,
        author=author,
        title=title,
        year=year,
        series=series,
        pages=pages,
        error=error_message,
    )


@app.route("/article", methods=["GET", "POST"])
def article():
    """Render the article form and recieve form inputs"""
    reference_name = ""
    title = ""
    author = ""
    year = ""
    journal = ""
    pages = ""
    error_message = None

    if request.method == "POST":
        reference_name = request.form.get("reference_name")
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")
        journal = request.form.get("journal")
        pages = request.form.get("pages")

        try:
            year_int = parse_year(year)
        except ValueError as err:
            error_message = str(err)
        else:
            add_article(db, reference_name, title,
                        author, year_int, journal, pages)

    return render_template(
        "article.html",
        author=author,
        title=title,
        year=year,
        error=error_message
    )


@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book_route(book_id):
    """Delete a book."""
    delete_book(db, book_id)
    return redirect(url_for("index"))


@app.route("/book/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book_route(book_id):
    """Edit a book."""
    book_to_edit = get_book(db, book_id)
    if book_to_edit is None:
        abort(404)

    if request.method == "POST":
        reference_name = request.form.get("reference_name")
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")
        publisher = request.form.get("publisher")

        try:
            year_int = parse_year(year)
        except ValueError as err:
            error_message = str(err)
        else:
            edit_book(db, book_id, reference_name,
                      title, author, year_int, publisher)
            return redirect(url_for("index"))

        book_to_edit = {
            "id": book_id,
            "reference_name": reference_name,
            "title": title,
            "author": author,
            "year": year,
            "publisher": publisher
        }
    else:
        error_message = None

    return render_template(
        "book.html",
        book=book_to_edit,
        is_edit=True,
        reference_name=book_to_edit["reference_name"],
        author=book_to_edit["author"],
        title=book_to_edit["title"],
        year=book_to_edit["year"],
        publisher=book_to_edit["publisher"],
        error=error_message
    )


@app.route("/article/<int:article_id>/delete", methods=["POST"])
def delete_article_route(article_id):
    """Delete an article."""
    delete_article(db, article_id)
    return redirect(url_for("index"))


@app.route("/inproceedings/<int:inproceedings_id>/delete", methods=["POST"])
def delete_inproceedings_route(inproceedings_id):
    """Delete an inproceedings."""
    delete_inproceedings(db, inproceedings_id)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
