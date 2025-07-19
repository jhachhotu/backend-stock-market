import sqlite3
import yfinance as yf

def get_db_connection():
    """
    Establishes a connection to the SQLite database and enables row access as dictionaries.
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_stock_data(symbol):
    """
    Fetches 5-day stock price data from Yahoo Finance using yfinance.

    Returns:
        dict: {
            "dates": list of formatted dates (YYYY-MM-DD),
            "prices": list of closing prices
        }
    """
    try:
        df = yf.download(symbol, period="5d", interval="1d")

        if df.empty:
            return {
                "dates": [],
                "prices": []
            }

        # Return dates and close prices
        return {
            "dates": df.index.strftime('%Y-%m-%d').tolist(),
            "prices": df['Close'].fillna(0).tolist()
        }

    except Exception as e:
        # Return error info if fetching fails
        return {
            "dates": [],
            "prices": [],
            "error": str(e)
        }
