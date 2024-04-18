from flask import Flask, render_template, send_from_directory, redirect, request
from flask_sqlalchemy import SQLAlchemy
from mtranslate import translate

app = Flask(__name__, static_url_path='/static')

app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class AddressBook(db.Model):
    __tablename__ = 'address_book'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    patronymic = db.Column(db.String(128))
    birthday = db.Column(db.Date)
    address = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    notes = db.Column(db.Text)

    def __init__(self, last_name, first_name, patronymic, birthday, address, phone, notes):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birthday = birthday
        self.address = address
        self.phone = phone
        self.notes = notes


class Professions(db.Model):
    __tablename__ = 'professions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name


class Characteristics(db.Model):
    __tablename__ = 'characteristics'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(128), nullable=False)
    education = db.Column(db.String(128))
    profession = db.Column(db.String(128))
    qualification = db.Column(db.String(128))
    work_experience = db.Column(db.String(128))

    def __init__(self, last_name, education, profession, qualification, work_experience):
        self.last_name = last_name
        self.education = education
        self.profession = profession
        self.qualification = qualification
        self.work_experience = work_experience



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    role = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Integer, unique=True, nullable=True)

    def __init__(self, email, username, role, active):
        self.email = email
        self.username = username
        self.role = role
        self.active = active


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    translation = db.Column(db.String(100), nullable=False)

    def __init__(self, word, translation):
        self.word = word
        self.translation = translation


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        existing_word = Word.query.filter_by(word=word).first()
        if existing_word:
            pass
        else:
            translated_word = translate(word, 'uk')
            new_word = Word(word=word, translation=translated_word)
            db.session.add(new_word)
            db.session.commit()
    if request.method == 'GET':
        delete_word_id = request.args.get('delete_word_id')
        if delete_word_id:
            word_to_delete = Word.query.get(delete_word_id)
            if word_to_delete:
                db.session.delete(word_to_delete)
                db.session.commit()

    words = Word.query.all()
    return render_template('index.html', words=words)


@app.route("/dashboard")
def dashboard():
    select_all = User.query.filter_by(username='pashka').first()
    email = select_all.email
    return render_template('dashboard.html', email=email)


@app.route("/table")
def table():
    select_all = User.query.filter_by(username='pashka').first()
    email = select_all.email
    return render_template('table.html')


@app.route("/context_words")
def context_words():
    return render_template('context_words.html')


@app.route("/verbs")
def verbs():
    return render_template('verbs.html')


if __name__ == "__main__":
    app.run(debug=True)
