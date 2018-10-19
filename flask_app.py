
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="altus",
    password="password",
    hostname="altus.mysql.pythonanywhere-services.com",
    databasename="altus$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

comments = []

@app.route("/", methods=("GET","POST"))
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    #comments.append(request.form["contents"])
    return redirect(url_for("index"))


#Leave this for the A7 tracker
@app.route("/location", methods=("POST",))
def submit_location_data():
    if request.method == "POST":
        lat = request.form.get("lat")
        lng = request.form.get("lng")
        data = (lat, lng)
    else:
        data = "error"
    return str(data)

