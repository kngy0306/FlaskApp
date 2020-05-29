from flask import Flask, render_template, request, url_for
import scraping

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('layout.html', title='Scraping App')


@app.route('/scraping')
def get():
    return scraping.scraping()


if __name__ == "__main__":
    app.run(debug=True)
