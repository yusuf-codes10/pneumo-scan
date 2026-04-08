from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def send_prediction():
    return '<h1>Nothing to send</h1>'

if __name__ in "__main__":
    app.run(debug=True)