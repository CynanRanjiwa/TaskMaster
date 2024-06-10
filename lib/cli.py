import click
from sqlalchemy.orm import sessionmaker
from models import Task, Category, User, engine

Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Task Manager CLI"""
    pass

@cli.command()
@click.option('--title', prompt='Task title', help='The title of the task.')
@click.option('--description', prompt='Task description', help='Description of the task.')
def add_task(title, description):
    """Add a new task."""
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    click.echo(f'Task "{title}" added.')

@cli.command()
def view_tasks():
    """View all tasks."""
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} - {task.description} (Status: {task.status})')

if __name__ == '__main__':
    cli()


"""import click
from sqlalchemy.orm import sessionmaker
from db.models import engine, Task, User, Category

Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Task Manager CLI"""


@cli.command()
@click.option('--title', prompt='Task title', help='The title of the task.')
@click.option('--description', prompt='Task description', help='Description of the task.')
def add_task(title, description):
"""Add a new task."""
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    click.echo(f'Task "{title}" added.')

@cli.command()
@click.option('--title', prompt='Task title', help='The title of the task.')
@click.option('--description', prompt='Task description', help='Description of the task.')
@click.option('--user', prompt='User ID', help='ID of the user responsible for the task.')
@click.option('--category', prompt='Category ID', help='ID of the task category.')
def add_task(title, description, user, category):
    """Add a new task."""
    new_task = Task(title=title, description=description, user_id=user, category_id=category)
    session.add(new_task)
    session.commit()
    click.echo(f'Task "{title}" added.')

@cli.command()
def view_tasks():
    """View all tasks."""
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} - {task.description} (Status: {task.status})')

if __name__ == '__main__':
    cli()
"""