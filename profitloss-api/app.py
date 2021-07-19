import flask
import db_connect
import simplejson
from db_connect import database
from flask import Flask, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/getAllEntries", methods = ["GET"])
def getAllEntries():
    connection = database()
    cursor = database.connect()

    cursor.execute("SELECT * from profits")
    results = cursor.fetchall()
    return simplejson.dumps(results)


if __name__ == "__main__":
    app.run()
