from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    mars_things = mongo.db.mars_things.find_one()
    return render_template("index.html", mars_things=mars_things)


@app.route("/scrape")
def scrape():
    mars_things = mongo.db.mars_things
    mars_data = scrape_mars.scrape()
    mars_things.update(
        {},
        mars_data,
        upsert=True
    )
    return "Scraped successfully!"


if __name__ == "__main__":
    app.run(debug=True)


