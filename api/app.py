from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/hello")
def hello():
    return {"message": "Hello from API"}

@app.route("/db-test")
def db_test():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    conn.close()
    return {"status": "Database connection successful"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)