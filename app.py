import json
from flask import Flask, request, jsonify
import os
import razorpay

app = Flask(__name__)
client = razorpay.Client(auth=("rzp_test_nFKekgDUCv55L4", "onfHa3ohp93LrIt01HHYYUWc"))

@app.route('/create_order', methods=['POST'])
def create_order():
  req_data = request.args
  amount = req_data['amount']
  currency = req_data['currency']
  receipt = req_data['receipt']
  # notes = req_data['notes']

  order_data = {
    "amount": amount,
    "currency": currency,
    "receipt": receipt,
    "notes": {
      "address": "Hello World"
    }
  }

  try:
    order = client.order.create(order_data)
    return order, 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route('/fetch_payment', methods=['POST'])
def fetch_payment(paymentId):
  try:
    payment = client.payment.fetch(paymentId)
    return payment, 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)
