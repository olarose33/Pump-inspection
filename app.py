from flask import Flask
import csv

app = Flask(__name__)

@app.route("/")
def home():
    with open("data/pump_sample.csv", newline="") as file:
        rows = list(csv.DictReader(file))

    return f"<h1>Pump Health Checker</h1><pre>{rows}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
