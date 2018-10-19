
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
app.config["DEBUG"] = False

comments = []

@app.route("/", methods=("GET","POST"))
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
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

