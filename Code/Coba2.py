from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if 'smoke_detected' in data:
        smoke_detected = data['smoke_detected']
        print(f"Received smoke detected: {smoke_detected}")

        # Anda dapat menambahkan logika untuk menangani data sensor di sini

        response = {
            "status": "success",
            "message": "Data received",
            "smoke_detected": smoke_detected
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "fail",
            "message": "Invalid data"
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
