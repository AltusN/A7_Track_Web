
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello_world():
    return render_template("main_page.html")


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

