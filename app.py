from flask import Flask, request, render_template
#import sqlite3
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def landing():
    if request.method == 'POST':
        request.form["email"]
        request.form["password"]
        return render_template("index.html")
    else:
        return render_template("login.html")
    

@app.route("/index.html")
def home():
    #df.columns = df.columns.str.strip()
    return render_template("index.html",data=data)

@app.route("/data.html")
def data():
    df = pd.read_csv("Teen_Mental_Health_Dataset.csv")
    data = [
        "age", "gender", "daily_social_media_hours", "platform_usage","sleep_hours","screen_time_before_sleep","academic_perfomance",
    ]
    data = df.to_dict(orient="records")
    return render_template("data.html",data=data)

@app.route("/login.html")
def login():
    return render_template("login.html")


@app.route("/register.html")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)