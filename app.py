from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello():
    return render_template('under_construction.html')


if __name__ == '__main__':
    app.run()
