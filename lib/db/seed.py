# adds initial entries to my databse tables for testing purposes
# populates the database with initial test data 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import Task, Category, User, engine
from .connection import engine

Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    db = Session(bind=engine)
    try:
        # Example data
        user = User(username="Cynan", email="Cynan@example.com", hashed_password="fakehashedpassword")
        category = Category(name="Work")
        task = Task(title="Finish report", description="Complete the quarterly report", priority=1, owner=user, category=category)
        
        db.add(user)
        db.add(category)
        db.add(task)
        
        db.commit()
        print("Database seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()