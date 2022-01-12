from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from flask.wrappers import Request

app = Flask(__name__)

rooms = {
    "room1": [],
    "room2": [],
    "room3": []
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rooms")
def roomDisplay():
    #returns number of rooms existing in the server
    result = {}
    for room_name in rooms:
        result[room_name] = len(rooms[room_name])
    
    return result

@app.route("/createRoom", methods=["POST"])
def createRoom():
    #creates a room based on the input given by the User
    """
    Input: room_name
    Output: rooms[room_name] = []
    """
    #data from the user
    room = request.json["room"]

    #check if room with given name already exists
    if room in rooms:
        return "Room already exists"

    rooms[room] = []
    return "OK"

@app.route("/sndmsg", methods=["POST"])
def sendMessage():
    #Store message in server
    """
    Input: room_name, message
    Output: rooms[room_name] = message
    """
    
    room = request.json["room"]
    message = request.json["message"]

    #check if room is not in rooms
    if room not in rooms:
        return "Invalid Room"
    
    rooms[room].append(message)

    return "OK"

@app.route("/msg")
def display():
    #display the message
    """
    Input: room_name,
    Output: rooms[room_name]
    """

    #get user data
    room = request.args["room"]

    #check if room is not in rooms
    if room not in rooms:
        return "Invalid Room"
    
    return jsonify(rooms[room])