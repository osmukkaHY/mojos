"""Main file for reference tool"""

from flask import Flask, request, render_template

app = Flask(__name__)

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
    return render_template("form.html", author=author, title=title, year=year)

if __name__ == '__main__':
    app.run()
