from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return make_response("Flask app is working",201)

if __name__ == '__main__':

    app.run(port=5000, debug=True)
