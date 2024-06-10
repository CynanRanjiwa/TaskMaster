from .connection.py import engine 
from ..models import Base
#create all tables in the database
def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database created")
    return True
if __name__ == "__main__":
    initialize_database()
    # this script connects to the database and creates the necessary tables 
    # running 'setup.py' directly will set up the database schema 

    # if you want to drop the database and recreate it, you can run:
    # drop_database()
    # initialize_database()