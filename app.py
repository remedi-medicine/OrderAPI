from flask import Flask, request, jsonify
import os
import razorpay

app = Flask(__name__)
client = razorpay.Client(auth=("rzp_test_nFKekgDUCv55L4", "onfHa3ohp93LrIt01HHYYUWc"))

@app.route('/create_order', methods=['POST'])
def create_order():
  req_data = request.get_json()
  print(req_data)
  amount = req_data['amount']
  currency = req_data['currency']
  receipt = req_data['receipt']
  notes = req_data['notes']
  print(amount, currency, receipt, notes)

  order_data = {
    "amount": 100*987,
    "currency": "INR",
    "receipt": "recipt#01",
    "notes": {
      name: "Burhanuddin Fatehi"
    }
  }

  try:
    order = client.order.create(order_data)
    return order, 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)
