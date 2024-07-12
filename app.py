from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Scholarship():
    return render_template("scholarship.html")

if __name__ == "__main__":
    app.run(debug=True)