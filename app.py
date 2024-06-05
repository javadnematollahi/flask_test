from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/", methods=['GET'])
def my_root():
    name = "javad"
    return render_template("index.html", name=name, x=10)

@app.route("/download", methods=['GET'])
def download():
    media = ["media", "music", "video"]
    return render_template("download.html", media=media)

@app.route("/me")
def my_information():
    info = {"firstname":"javad", "email":"javad7189@yahoo.coom"}
    return info

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "this is GET method"
    elif request.method == "POST":
        return "this is POST method"