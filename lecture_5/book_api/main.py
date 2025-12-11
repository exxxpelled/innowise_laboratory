from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Book, get_db 

# Create FastAPI application instance
app = FastAPI()


# POST /books/ - Add a new book to the collection
@app.post("/books/")
def add_book(book: dict, db: Session = Depends(get_db)):
    """
    Adds a new book to the database.
    
    Parameters:
    - book (dict): Dictionary with book data, must contain 'title' and 'author'
    
    Returns:
    - dict: Added book data with assigned ID
    """
    # Create a new Book instance with data from request
    new_book = Book(
        title=book["title"],
        author=book["author"],
        year=book.get("year")  # Year is optional
    )
    # Add book to database session
    db.add(new_book)
    # Commit transaction to save book in database
    db.commit()
    # Refresh book instance to get database-generated ID
    db.refresh(new_book)
    # Return book data as JSON response
    return {
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
        "year": new_book.year
    }


# GET /books/ - Retrieve all books from the collection
@app.get("/books/")
def get_all_books(db: Session = Depends(get_db)):
    """
    Retrieves all books from the database.
    
    Returns:
    - list: List of all books with their details
    """
    # Query all books from database
    books = db.query(Book).all()
    # Convert SQLAlchemy objects to dictionaries for JSON response
    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year": b.year
        }
        for b in books
    ]


# DELETE /books/{book_id} - Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Deletes a book by its ID.
    
    Parameters:
    - book_id (int): ID of the book to delete
    
    Returns:
    - dict: Confirmation message
    """
    # Find book by ID
    book = db.query(Book).filter(Book.id == book_id).first()
    
    # If book not found, return 404 error
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Delete book from database
    db.delete(book)
    # Commit transaction
    db.commit()
    
    # Return success message
    return {"message": "Book deleted"}


# PUT /books/{book_id} - Update book details
@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: dict, db: Session = Depends(get_db)):
    """
    Updates book details.
    
    Parameters:
    - book_id (int): ID of the book to update
    - book_data (dict): Dictionary with fields to update
    
    Returns:
    - dict: Updated book data
    """
    # Find book by ID
    book = db.query(Book).filter(Book.id == book_id).first()
    
    # If book not found, return 404 error
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update only the fields that were provided in request
    if "title" in book_data:
        book.title = book_data["title"]
    if "author" in book_data:
        book.author = book_data["author"]
    if "year" in book_data:
        book.year = book_data["year"]
    
    # Commit changes to database
    db.commit()
    # Refresh book instance to get updated data
    db.refresh(book)
    
    # Return updated book data
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }


# GET /books/search/ - Search books by title, author, or year
@app.get("/books/search/")
def search_books(
    title: str = None,
    author: str = None,
    year: int = None,
    db: Session = Depends(get_db)
):
    """
    Searches books by title, author, or year.
    
    Parameters:
    - title (str, optional): Title to search for (partial match)
    - author (str, optional): Author to search for (partial match)
    - year (int, optional): Publication year to search for (exact match)
    
    Returns:
    - list: List of matching books
    """
    # Start with base query for all books
    query = db.query(Book)
    
    # Add filters based on provided search parameters
    if title:
        # Search for title containing the provided string (case-sensitive)
        query = query.filter(Book.title.contains(title))
    if author:
        # Search for author containing the provided string (case-sensitive)
        query = query.filter(Book.author.contains(author))
    if year:
        # Search for exact year match
        query = query.filter(Book.year == year)
    
    # Execute query and get results
    books = query.all()
    
    # Convert results to dictionaries for JSON response
    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year": b.year
        }
        for b in books
    ]