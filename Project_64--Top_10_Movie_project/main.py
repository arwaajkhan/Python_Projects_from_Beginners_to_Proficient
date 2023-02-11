from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

tmdb_url = "https://api.themoviedb.org/3/search/movie?"


# CREATE UPDATE-FORM
class UpdateForm(FlaskForm):
    rating_field = FloatField(label="Your Rating Out of 10 e.g 7.5",
                              validators=[DataRequired(message='float value is only acceptable')])
    review_field = StringField(label="Your Review", validators=[DataRequired()])
    submit_field = SubmitField(label="Done")


# CREATE ADD-MOVIE-FORM
class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit_button = SubmitField(label="Add a Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    update_form = UpdateForm()
    movie_id = request.args.get('id')
    print(movie_id)
    movie = Movie.query.get(movie_id)
    print(movie)
    if update_form.validate_on_submit():
        movie.rating = update_form.rating_field.data
        movie.review = update_form.review_field.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=update_form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        parameter = {
            "api_key": "YOUR_API_KEY",
            "language": "en-US",
            "query": add_form.movie_title.data
        }
        response = requests.get(url=tmdb_url, params=parameter)
        contents = response.json()["results"]
        return render_template('select.html', movies_list=contents)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find():
    movie_api_id = request.args.get('movie_id')
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}?"
        parameter = {
            "api_key": "YOUR_API_KEY",
            "language": "en-US",
        }
        response = requests.get(url=movie_api_url, params=parameter).json()
        new_movie = Movie(
            title=response["title"],
            year=response["release_date"].split("-")[0],
            description=response["overview"],
            img_url=f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))  # This id you are passing from here to the edit function it
        # works same as when you click on update page and pass id as same name "id"


if __name__ == '__main__':
    app.run(debug=True)
