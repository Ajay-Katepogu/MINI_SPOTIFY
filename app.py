from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    songs = []

    if request.method == "POST":
        song = request.form.get("song")

        if song:
            url = "https://itunes.apple.com/search"

            params = {
                "term": song,
                "media": "music",
                "limit": 10
            }

            response = requests.get(url, params=params)
            data = response.json()

            songs = data.get("results", [])

    return render_template("index.html", songs=songs)


if __name__ == "__main__":
    app.run(debug=True)