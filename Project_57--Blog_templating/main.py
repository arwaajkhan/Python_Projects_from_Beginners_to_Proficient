from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/d96d079bc9d52e0d7c72").json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", id=blog_id, posts=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
