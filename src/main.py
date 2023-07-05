from database import Database
from notifier import Notifier
import typer, arrow, dotenv
from plan import Plan

CONFIG = dotenv.dotenv_values('.env')

DATABASE: str = CONFIG['database']
USERNAME: str = CONFIG['username']
PASSWORD: str = CONFIG['password']

db = Database(DATABASE)
app = typer.Typer()

@app.command()
def add(name: str, due_date: str = arrow.utcnow()):
    """Add a plan into the database."""
    try:
        plan = Plan(name, arrow.get(due_date))
        db.write(db.read() + [plan])
        typer.echo(plan)
    except arrow.ParserError:
        typer.echo('The time was not correctly formatted.')

@app.command()
def delete(name: str):
    """Remove a plan from the database by name."""
    db.write(filter(lambda plan: plan.name != name, db.read()))

@app.command()
def list():
    """List out all active plans."""
    plans = db.read()
    if len(plans) == 0:
        typer.echo(f'No plans set!')

    for idx, plan in enumerate(plans):
        typer.echo(f'{idx} :: {plan}')

@app.command()
def edit(idx: int, name: str = None, due_date: str = None):
    """Edit an already created plan."""
    plans = db.read()
    for i, _ in enumerate(plans):
        if idx == i:
            if name is not None:
                plans[i].name = name
            if due_date is not None:
                plans[i].due_date = arrow.get(due_date)
    db.write(plans)

@app.command()
def listen():
    """Notify user when a plan is due. Or when the user receives an email."""
    Notifier(db, USERNAME, PASSWORD).listen()


if __name__ == '__main__':
    app()
