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


"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Task

engine = create_engine('sqlite:///task_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# Add sample users
user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email='bob@example.com')
session.add_all([user1, user2])
session.commit()

# Add sample categories
category1 = Category(name='Work')
category2 = Category(name='Personal')
session.add_all([category1, category2])
session.commit()

# Add sample tasks
task1 = Task(title='Complete CLI project', description='Finish the CLI by end of the week', due_date='2024-06-14', status='Pending', priority='High', user_id=user1.id, category_id=category1.id)
task2 = Task(title='Grocery shopping', description='Buy groceries for the week', due_date='2024-06-12', status='Pending', priority='Medium', user_id=user2.id, category_id=category2.id)
session.add_all([task1, task2])
session.commit()"""