from dotenv import load_dotenv
from flask import Flask, render_template
import requests, os 

load_dotenv()

key_ = os.getenv('KEY_')
app = Flask(__name__)



@app.route("/")
def index():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key_}"
    response = requests.get(url)
    data = response.json()
    noticias = data["articles"]
    return render_template("index.html", noticias=noticias)

@app.route("/technology")
def technologies():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={key_}"
    response = requests.get(url)
    data = response.json()
    technologies = data["articles"]
    return render_template("technology.html", technologies=technologies)

if __name__ == "__main__":
    app.run(debug=True)
