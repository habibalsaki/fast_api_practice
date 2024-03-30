from fastapi import FastAPI

books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Fiction"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "category": "Science Fiction"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "category": "Romance"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Classic"
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "category": "Coming-of-age"
    }
]

app = FastAPI()

@app.get("/books")
async def get_books():
    return books

@app.get("/books/{title}")
async def get_book_by_title(title: str):
    for book in books:
        if book["title"].casefold() == title.casefold():
            return book
