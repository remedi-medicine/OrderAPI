from flask import Flask, request, jsonify
import os
import razorpay

app = Flask(__name__)
client = razorpay.Client(auth=(os.getenv('key_id'), os.getenv('key_secret')))

@app.route('/create_order', methods=['POST'])
def create_order():
  req_data = request.get_json()

  amount = req_data['amount']
  currency = req_data['currency']
  receipt = req_data['receipt']
  notes = req_data['notes']

  order_data = {
    "amount": amount,
    "currency": currency,
    "receipt": receipt,
    "notes": notes
  }

  try:
    order = client.order.create(order_data)
    return order, 200
  except razorpay.errors.RazorpayError as e:
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)
