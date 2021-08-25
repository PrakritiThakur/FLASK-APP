from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        "id":1 ,
        "name":u'Prakriti Thakur',
        "contact":u"7879514196",
        "done":False,
    },
    {
        "id":2 ,
        "name":u'Ranjana Thakur',
        "contact":u"9340914533",
        "done":False,
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    task = {
        "id": tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact": request.json["contact"],
        "done" : False,
    }

    tasks.append(task)

    return jsonify({
        "status":"success",
        "message":"Contact saved"
    })

@app.route("/app-data")

def get_task():
    return jsonify({
        "data" : tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)