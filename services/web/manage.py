from flask.cli import FlaskGroup
from flask_migrate import Migrate
from project import app, db, User, Word, AddressBook, Professions, Characteristics

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
    # Додавання даних до таблиці address_book
    address_entries = [
        AddressBook(last_name="Петренко",first_name="Петро",patronymic="Олексійович",birthday="2002-12-09",address="І. Уржайка, 27/8",phone="21-24-25",notes=""),
        AddressBook(last_name="Коваленко",first_name="Інна",patronymic="Андріївна",birthday="1995-05-14",address="С. Юрій, 78/8",phone="45-14-14",notes=""),
        AddressBook(last_name="Симоненко",first_name="Семен",patronymic="Борисович",birthday="1987-07-23",address="Соборна, 48/78",phone="54-24-79",notes=""),
        AddressBook(last_name="Балашов", first_name="Борис", patronymic="Миколайович", birthday="1981-08-16",address="П. Запорожця, 23/8", phone="62-42-99", notes=""),
        AddressBook(last_name="Шаріков", first_name="Олег", patronymic="Васильович", birthday="1970-08-31",address="Келецька, 45/78", phone="64-78-88", notes=""),
        AddressBook(last_name="Дончук", first_name="Олексій", patronymic="Леонідович", birthday="1985-05-14",address="Бучми, 45", phone="44-78-66", notes="")
    ]
    professions = [
        Professions(name='DevOps'),
        Professions(name='QA'),
        Professions(name='Product Manager'),
        Professions(name='CEO'),
        Professions(name='Developer'),
        Professions(name='Data Science')
    ]
    characteristics = [
        Characteristics(last_name="Мазепа",education="Вища, Магістр інформатики",profession="Програміст",qualification="Senior Software Developer",work_experience="5 років в розробці програмного забезпечення"),
        Characteristics(last_name="Шевченко",education="Бакалавр менеджменту",profession="Керівник проекту",qualification="PMP сертифікований",work_experience="3 роки керівництва проектними командами"),
        Characteristics(last_name="Квітка",education="Бакалавр філології",profession="Перекладач",qualification="Спеціаліст із англійської та німецької мов",work_experience="4 роки перекладацької діяльності"),
        Characteristics(last_name="Петренко",education="Вища, Магістр економіки",profession="Фінансовий аналітик",qualification="CFA Level II кандидат",work_experience="6 років в аналізі ринкових тенденцій"),
        Characteristics(last_name="Українка",education="Бакалавр образотворчого мистецтва",profession="Графічний дизайнер",qualification="Експерт Adobe Creative Suite",work_experience="7 років створення візуального контенту"),
    ]
    db.session.bulk_save_objects(address_entries)
    db.session.bulk_save_objects(professions)
    db.session.bulk_save_objects(characteristics)


    db.session.add(User(email="sytnikp1@gmail.com", username="pashka", role="admin", active=1))
    db.session.add(User(email="sytnik.p@gmail.com", username="sytnik", role="user", active=0))


    db.session.commit()



if __name__ == "__main__":
    cli()
