import mariadb
from flask import Flask, request, Response
import json
import dbcreds
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/todo', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def todo():
    if request.method == 'GET':
        conn = None
        cursor = None
        todo_items = None
        try:
            conn = mariadb.connect(host = dbcreds.host, password = dbcreds.password, user = dbcreds.user, port = dbcreds.port, database = dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todo_items")
            todo_items = cursor.fetchall()
        except Exception as error:
            print("Something went wrong (not good practice): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(todo_items != None):
                return Response(json.dumps(todo_items, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong...please try again", mimetype = "text/html", status = 500)
    elif request.method == 'POST':
        conn = None
        cursor = None
        item_description = request.json.get("description")
        item_created_at = request.json.get("created_at")
        rows = None
        try:
            conn = mariadb.connect(host = dbcreds.host, password = dbcreds.password, user = dbcreds.user, port = dbcreds.port, database = dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todo_items(description, created_at) VALUES(?, ?)", [item_description, item_created_at,])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (not good practice): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Task has been added!", mimetype = "text/html", status = 201)
            else:
                return Response("Something went wrong... please try again", mimetype = "text/html", status = 500)
    elif request.method == 'PATCH':
        conn = None
        cursor = None
        rows = None
        item_description = request.json.get("description")
        item_completed = request.json.get("completed")
        item_id = request.json.get("id")
        try:
            conn = mariadb.connect(host = dbcreds.host, password = dbcreds.password, user = dbcreds.user, port = dbcreds.port, database = dbcreds.database)
            cursor = conn.cursor()
            if(item_description != "" and item_description != None):
                cursor.execute("UPDATE todo_items SET description = ? WHERE id = ?", [item_description, item_id,])
            if(item_completed != "" and item_completed != None):
                cursor.execute("UPDATE todo_items SET completed = ? WHERE id = ?", [item_completed, item_id,])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (not good practice): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Task has been updated!", mimetype = "text/html", status = 204)
            else:
                return Response("Something went wrong... please try again", mimetype = "text/html", status = 500)
    elif request.method == 'DELETE':
        conn = None
        cursor = None
        rows = None
        item_id = request.json.get("id")
        try:
            conn = mariadb.connect(host = dbcreds.host, password = dbcreds.password, user = dbcreds.user, port = dbcreds.port, database = dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todo_items WHERE id = ?", [item_id,])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (not good practice): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Task has been deleted!", mimetype = "text/html", status = 200)
            else:
                return Response("Something went wrong... please try again", mimetype = "text/html", status = 500)