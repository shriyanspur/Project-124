from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact": "9987644456",
        "Name": 'Raju',
        "ID": 1,
        "Done": False
    },
    {
        "Contact": "9876543222",
        "Name": 'Rahul',
        "ID": 2,
        "Done": False
    },
]


@app.route('/add-data', methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "Please provide the data" 
        },
        400
        )
    task = { 
        'ID': contacts[-1]['ID'] + 1,
        'Title': request.json['Title'],
        'Description': request.json.get('Description', ""),
        'Done': False 
    } 
    contacts.append(task)
    return jsonify({ 
        "status":"success",
        "message": "Task added succesfully!" 
    })

@app.route("/get-data") 
def get_task(): 
    return jsonify({ 
        "data" : contacts
    })

if(__name__ == '__main__'):
    app.run(debug=True)