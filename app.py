from flask import Flask, request, jsonify

app = Flask(__name__)

# Celsius to Fahrenheit conversion
@app.route('/convert/celsius_to_fahrenheit', methods=['GET'])
def celsius_to_fahrenheit():
    try:
        celsius = float(request.args.get('celsius'))
        fahrenheit = (celsius * 1.8) + 32
        return jsonify({
            'celsius': celsius,
            'fahrenheit': fahrenheit
        })
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input for Celsius temperature.'}), 400

# BMI calculator
@app.route('/calculate/bmi', methods=['GET'])
def calculate_bmi():
    try:
        weight = float(request.args.get('weight'))
        height = float(request.args.get('height'))
        if height <= 0:
            return jsonify({'error': 'Height must be greater than zero.'}), 400
        bmi = weight / (height ** 2)
        return jsonify({
            'weight': weight,
            'height': height,
            'bmi': bmi
        })
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input for weight or height.'}), 400

# Loan calculator
@app.route('/calculate/loan_payment', methods=['GET'])
def calculate_loan_payment():
    try:
        principal = float(request.args.get('principal'))
        annual_interest = float(request.args.get('annual_interest'))
        years = int(request.args.get('years'))

        monthly_interest = annual_interest / 1200
        number_of_payments = years * 12

        if monthly_interest == 0:
            monthly_payment = principal / number_of_payments
        else:
            monthly_payment = principal * monthly_interest / (1 - (1 + monthly_interest) ** -number_of_payments)

        return jsonify({
            'principal': principal,
            'annual_interest': annual_interest,
            'years': years,
            'monthly_payment': monthly_payment
        })
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input for loan calculation.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
