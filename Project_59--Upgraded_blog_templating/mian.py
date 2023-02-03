import requests
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/daf3837d0afbcbb02f06").json()
my_email = "appbreweryinfo3144@gmail.com"
password = "ulogjjmvqiewhlsh"


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', message="Message sent successfully")
    return render_template('contact.html')


def send_email(name, email, phone, message):
    email_message = f'Subject: Project(60) Demo\n\nName: {name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, my_email, email_message)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    sending_post = None
    for blog_post in all_posts:
        if blog_post["id"] == blog_id:
            sending_post = blog_post
    return render_template('post.html', post=sending_post)


if __name__ == "__main__":
    app.run(debug=True)
