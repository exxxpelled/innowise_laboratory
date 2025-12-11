from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker  

# Database connection URL for SQLite
# 'sqlite:///./books.db' creates a SQLite database file named 'books.db' in current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# Create declarative base class - all ORM models will inherit from this
Base = declarative_base()

# Define Book model - represents the 'books' table in database
class Book(Base):
    # Table name in database
    __tablename__ = "books"
    
    # Define columns with SQLAlchemy types and constraints
    # id: Primary key, automatically indexed for faster queries
    id = Column(Integer, primary_key=True, index=True)
    
    # title: Required string field (cannot be NULL in database)
    title = Column(String, nullable=False)
    
    # author: Required string field (cannot be NULL in database)
    author = Column(String, nullable=False)
    
    # year: Optional integer field (can be NULL in database)
    year = Column(Integer, nullable=True)

# Create all tables defined by models that inherit from Base
Base.metadata.create_all(bind=engine)

# Dependency function for FastAPI to get database session
def get_db():
    # Create new database session
    db = SessionLocal()
    try:
        # Yield session to endpoint function
        yield db
    finally:
        # Always close session when done, even if error occurs
        db.close()