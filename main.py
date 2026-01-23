from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("camera.html")

if __name__ == "__main__":
    app.run(debug=True)

#  key: 4bd22ff7ea42957482249eecce4833667eb6dee56f73c02f82cecce1425c89cd