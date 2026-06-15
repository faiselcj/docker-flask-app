from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="rootpass",
            database="appdb"
        )
        return "Connected to MySQL Successfully!"
    except Exception as e:
        return f"Connection Failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
