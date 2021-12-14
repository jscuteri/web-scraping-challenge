from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    marspage = mongo.db.red_planet.find_one()
    return render_template("index.html", red_planet=marspage)


@app.route("/scrape")
def scraper():
    red_planet = mongo.db.red_planet
    mars_data = scrape_mars.scrape()
    red_planet.replace_one({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
