from flask.cli import FlaskGroup
from flask_migrate import Migrate

from project import app, db, User

cli = FlaskGroup(app)
migrate = Migrate(app, db)
cli.add_command('db', Migrate)

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="sytnikp1@gmail.com", username="pashka", role="admin", active=1))
    db.session.add(User(email="sytnik.p@gmail.com", username="sytnik", role="user", active=0))
    db.session.add(User(email="sytnikp1@gmail.com", username="alexey", role="test", active=2))
    db.session.commit()


if __name__ == "__main__":
    cli()
