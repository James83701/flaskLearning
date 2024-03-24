from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'james',
        'title': 'first post',
        'content': 'first content',
        'date_posted': 'March 23rd, 2024'

    },
    {
        'author': 'jane',
        'title': 'second post',
        'content': 'second content',
        'date_posted': 'March 23rd, 2024'

    }
]


@app.route("/", methods = ['GET'])
@app.route("/home", methods = ['GET'])
def home():
    return render_template('home.html', posts = posts)


@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug = 'true')