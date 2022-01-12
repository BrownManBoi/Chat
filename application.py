from flask import Flask, render_template, request, redirect
from flask.json import jsonify

app = Flask(__name__)

rooms = {
    "room1": [],
    "room2": [],
    "room3": []
}

@app.route("/rooms")
def getRooms():
    result = {}
    for room_name in rooms:
        result[room_name] = len(rooms[room_name])
    return result

@app.route("/sndmsg", methods=["POST"])
def sendMessage():
    """
    Client will call server with /sendmsg and will pass this data:
    {
        "room": "room1",
        "message": "Hello world, thsi is my first message to the room"
    }
    """
    room = request.json["room"]
    msg = request.json["message"]

    # validation
    if room not in rooms:
        return "Invalid room"
    
    # data is valid.
    rooms[room].append(msg)    
    return "ok"

@app.route("/msg")
def display():
    """
    Input: room_name
    Output: rooms[room_name]
    """
    room = request.args["room"]

    if room not in rooms:
        return "Invalid room"

    return jsonify(rooms[room])

@app.route("/createRoom", methods=["POST"])
def createRoom():
    """
    Input: room_name
    Output: rooms[room_name] = []
    """
    # what is the input?
    # what is the output?
    # how to check if input is valid
    # rest of the logic

    room = request.json["room"]

    if room in rooms:
        return "Room already exists"

    rooms[room] = []
    return "ok"


# run with
# flask run --host=0.0.0.0