from crypt import methods
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, Blueprint

# from supabase import create_client, Client


# key: str = os.environ.get("SUPABASE_KEY")

# supabase: Client = create_client(url, key)

load_dotenv()  # loads variables from .env file into environment

bp = Blueprint("blog", __name__)
app = Flask(__name__)
url: str = os.environ.get("SUPABASE_URL")
# url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)


@app.route("/", methods=["GET", "POST"])
def home():
    return {"home": "This is the homepage"}


# CREATE ROUTE
@app.route("/api/room", methods=["GET", "POST"])
def create_room():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO rooms (name) VALUES ('{name}') RETURNING id;", (name,)
                )
    elif request.method == "GET":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM rooms")
                # transform result
                columns = list(cursor.description)
                result = cursor.fetchall()

                # make dict
                results = []
                for row in result:
                    row_dict = {}
                    for i, col in enumerate(columns):
                        row_dict[col.name] = row[i]
                    results.append(row_dict)
            return results
            # rooms = cursor.fetchall()
            # ans1 = []
            # for row in rooms:
            #     # ans1.append(dict(row))
            #     print(row)
            # print(ans1)
    # elif request.method == "DELETE":
    # return {"id": room_id, "message": f"Room {name} created."÷\}, 201


# INDEX ROUTE


# UPDATE ROUTE


# DELETE ROUTE
