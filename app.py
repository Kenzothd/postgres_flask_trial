import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()  # loads variables from .env file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

@app.route('/')
def home():
    return {"home":"This is the homepage"}


@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO rooms (name) VALUES ('{name}') RETURNING id;", (name,))
            room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"Room {name} created."}, 201


