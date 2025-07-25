from flask import Flask, request, render_template
import requests

app = Flask(__name__)

url = "https://cyberadvice.onrender.com/advices"

@app.route("/", methods = ["POST", "GET"])
def main():
    result = ""
    if request.method == "GET":
        response = requests.get(url)
        adv = response.json()["response"]

        if response.status_code == 200:
            result = adv
        else:
            result = "Try Again"
    return render_template("index.html", result = result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)