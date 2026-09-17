from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python Programming", "author": "John Smith", "status": "Available"},
    {"id": 2, "title": "Data Science Basics", "author": "David Brown", "status": "Available"},
    {"id": 3, "title": "Artificial Intelligence", "author": "Robert Lee", "status": "Issued"}
]

@app.route("/")
def home():
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(new_book)
    return redirect("/")


@app.route("/issue/<int:book_id>")
def issue_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book["status"] = "Issued"
    return redirect("/")


@app.route("/return/<int:book_id>")
def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book["status"] = "Available"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
