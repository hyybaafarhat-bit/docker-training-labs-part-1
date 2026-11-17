from flask import Flask

app = Flask(__name__)


@app.route("/")
def accueil():
    return "Version 1.2 : test du cache\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
