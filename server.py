from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("nihao")
    return "nihao"


if __name__ == "__main__":
    app.run(debug=True)
