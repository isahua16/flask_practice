from dbhelpers import run_statement
from flask import Flask, request, make_response, jsonify
import json
app = Flask(__name__)

def check_data(data_type, required_data):
    for data in required_data:
        if(data_type.get(data) == None):
            return f"The {data} parameter is missing."

@app.post('/api/client')
def create_client():
    error = check_data(request.json, ["username", "password", "is_premium"])
    if(error != None):
        return make_response(jsonify(error, 400))
    results = run_statement("CALL create_client(?,?,?)", [request.json.get("username"), request.json.get("password"), request.json.get("is_premium")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

@app.patch('/api/client')
def update_password():
    error = check_data(request.json, ["username", "old_password", "new_password"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement("CALL update_password(?,?,?)", [request.json.get("username"), request.json.get("old_password"), request.json.get("new_password")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

app.run(debug=True)
