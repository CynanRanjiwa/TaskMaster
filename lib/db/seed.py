from models import User, Category, Task, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///TaskMaster.db')
Session = sessionmaker(bind=engine)
session = Session()
# Add sample users, categories and tasks
user = user (name = "Cynan Wanjira", email = "cynan@gmail.com")
session.add(user)
session.commit()

category = category (name = "Work")
session.add(category)
session.commit()

task = Task(title='Complete project', description='Finish the CLI project',
            category_id=category.id, priority='High', status='Pending',
            user_id=user.id)
session.add(task)
session.commit()