from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'contact': u'9987644456',
        'name': u'Raju', 
        'done': False
        
    },
    {
        'id': 2,
        'contact': u'9876543222',
        'description': u'Rahul', 
        'done': False
        
    }
]

@app.route("/")
def hello_world():
    return "Im woody"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "data added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)             