from flask import Flask, render_template, request
import requests
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

app = Flask(__name__)

blog_url = 'https://api.npoint.io/6620ac1a4ab9ee5b23d4'
all_blogs = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html",blogs = all_blogs )

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        s.starttls()
        s.login("sender_email_id", "sender_email_id_password")
        message = f"Name: {request.form['name']}, email: {request.form['email']}, phone: {request.form['phone']}, message: {request.form['message']}"
        s.sendmail("sender_email_id", "receiver_email_id", message)
        s.quit()
        return render_template("contact.html", tex = f"Successfully sent your message.")
    elif request.method == 'GET':
        return render_template("contact.html", tex="Contact Me")

@app.route('/post/<int:post_id>')
def show_post(post_id):
    blog = all_blogs[post_id-1]
    img_name = f"assets/img/post-bg-{post_id}.jpg"
    return render_template("post.html", blog = blog, img_name=img_name)


if __name__ == "__main__":
    app.run()