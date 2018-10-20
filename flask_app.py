
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="altus",
    password="password123",
    hostname="altus.mysql.pythonanywhere-services.com",
    databasename="altus$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route("/", methods=("GET","POST"))
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    #This is wrong... must figure out why it's posting
    comment = None

    try:
        comment = Comment(content=request.form["contents"])
    except Exception:
        pass

    if comment:
        db.session.add(comment)
        db.session.commit()

    return redirect(url_for("index"))

@app.route("/login", methods=("GET","POST"))
def login():
    if request.method == "GET":
        return render_template("login_page.html", error=False)

    if request.form["username"] != "admin" or request.form["password"] != "secret":
        return render_template("login_page.html", error=True)

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

