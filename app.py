# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():

    try:
        number1 = float(request.args.get('number1', 0))  
        number2 = float(request.args.get('number2', 0))  
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

    
    sum_of_numbers = number1 + number2
    prediction = 1 if sum_of_numbers > 5.8 else 0

    
    response = {
        "prediction": prediction,
        "features": {
            "number1": number1,
            "number2": number2,
            "sum": sum_of_numbers
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
