from sqlachemy import create_engine 
from sqlalchemy.orm import sessionmaker
# update this with my desired database 
DATABASE_URL = 'sqlite://TaskMaster.db'

# create an engine to communicate with the sqlite database
engine = create_engine(DATABASE_URL, echo=True)
# create a configured "session" class 
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
#dependencies for getting the session
def get_db ():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

        # handles the creation of the databse engine and session management 
        