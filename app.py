from flask import Flask, jsonify, request
from flask_cors import CORS
from mock_data import get_stock_data, get_stock_by_symbol

app = Flask(__name__)
# Allow CORS for the frontend origin (adjust if your frontend runs elsewhere)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

@app.route('/')
def home():
    return 'Welcome to the Stock Data API!'

@app.route('/api/companies')
def get_companies():
    try:
        # Return the full stock data for all companies
        stocks = get_stock_data()
        return jsonify(stocks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    try:
        print(f"Getting data for: {symbol}")
        stock = get_stock_by_symbol(symbol)
        return jsonify(stock)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
