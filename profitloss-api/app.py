import flask
import db_connect
import simplejson
from db_connect import database
from flask import Flask, jsonify, request
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/getAllEntries", methods = ["GET"])
def getAllEntries():
    connection = database()
    cursor = database.connect()

    cursor.execute("SELECT * from profits")
    results = cursor.fetchall()
    return simplejson.dumps(results)

@app.route("/addProfitEntry", methods = ["POST"])
def addEntry():
    try:
        trader_name = request.args.get('name')
        profit_amount = request.args.get('profit')

        connection = database()
        cursor = database.connect()

        cursor.execute(f"INSERT INTO profits VALUES (DEFAULT, {trader_name}, {profit_amount})")
        cursor.execute("COMMIT")
        return "Data Added!"
    except:
        print("error")

if __name__ == "__main__":
    app.run()
