from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def send_prediction():
    pass

if __name__ in "__main__":
    app.run(debug=True)