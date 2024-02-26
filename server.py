from flask import Flask, request, abort

app = Flask(__name__)

events = []

@app.route("/", methods=["POST", "GET"])
def webhook():
    global events
    if request.method == "POST":
        print(request.json)
        events += [request.json]
        return "sucess", 200
    elif request.method == "GET":
        return events, 200
    else:
        abort(400)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
