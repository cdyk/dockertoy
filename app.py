from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def foo():
    input = request.json
    if input is None:
        input = {}
    cp = subprocess.run(["./main"],
                        input=bytes(json.dumps(input),'utf-8'),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    return cp.stdout

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
