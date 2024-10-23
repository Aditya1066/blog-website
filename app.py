from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/6620ac1a4ab9ee5b23d4'
all_blogs = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html",blogs = all_blogs )

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def show_post(post_id):
    blog = all_blogs[post_id-1]
    img_name = f"assets/img/post-bg-{post_id}.jpg"
    return render_template("post.html", blog = blog, img_name=img_name)

if __name__ == "__main__":
    app.run()
