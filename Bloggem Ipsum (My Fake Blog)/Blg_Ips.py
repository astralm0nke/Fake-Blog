from flask import Flask, render_template
from datetime import datetime
import requests

class BlogPost:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

BIN_API = 'https://api.npoint.io/a1e02e5c82b2374ee349'
posts = requests.get(BIN_API).json()
post_objects = []
for post in posts:
    post_components = BlogPost(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_components)
    
webblog = Flask(__name__)

@webblog.route('/')
def home_page():
    today = datetime.now()
    current_year = today.year
    return render_template('blog_index.html', year=current_year, all_posts=post_objects)

@webblog.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("blogpost.html", post=requested_post)

if __name__ == '__main__':
    webblog.run(debug=True)