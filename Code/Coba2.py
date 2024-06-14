from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if 'smoke_detected' in data:
        smoke_detected = data['deteksi_asap']
        print(f"Received smoke detected: {deteksi_asap}")

        response = {
            "status": "Berhasil",
            "message": "Data received",
            "smoke_detected": smoke_detected
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "fail",
            "message": "Data Salah"
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
