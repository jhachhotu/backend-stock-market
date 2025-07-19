from datetime import datetime, timedelta
from random import random
from typing import List, TypedDict

class ChartDataPoint(TypedDict):
    time: str
    price: float

class StockData(TypedDict):
    id: str
    symbol: str
    name: str
    currentPrice: float
    change: float
    changePercent: float
    chartData: List[ChartDataPoint]

def generate_stock_data(symbol: str, name: str, base_price: float) -> StockData:
    """Generate realistic stock price data for a given symbol."""
    chart_data = []
    current_price = base_price
    time_points = 30  # Last 30 data points
    
    for i in range(time_points, -1, -1):
        date = datetime.now() - timedelta(hours=i)
        
        # Generate realistic price movement (±2% volatility)
        volatility = (random() - 0.5) * 0.04
        current_price = current_price * (1 + volatility)
        
        chart_data.append({
            'time': date.strftime('%H:%M'),
            'price': round(current_price, 2)
        })
    
    final_price = chart_data[-1]['price']
    change = final_price - base_price
    change_percent = (change / base_price) * 100

    return {
        'id': symbol.lower(),
        'symbol': symbol,
        'name': name,
        'currentPrice': final_price,
        'change': round(change, 2),
        'changePercent': round(change_percent, 2),
        'chartData': chart_data
    }

# Sample stock data with realistic Indian stock market symbols and base prices
stocks_data = [
    generate_stock_data('RELIANCE', 'Reliance Industries Ltd', 2450.00),
    generate_stock_data('TCS', 'Tata Consultancy Services', 3650.00),
    generate_stock_data('INFY', 'Infosys Limited', 1420.00),
    generate_stock_data('HDFCBANK', 'HDFC Bank Limited', 1580.00),
    generate_stock_data('ICICIBANK', 'ICICI Bank Limited', 960.00),
    generate_stock_data('HINDUNILVR', 'Hindustan Unilever Ltd', 2380.00),
    generate_stock_data('SBIN', 'State Bank of India', 720.00),
    generate_stock_data('BHARTIARTL', 'Bharti Airtel Limited', 1150.00),
    generate_stock_data('ITC', 'ITC Limited', 420.00),
    generate_stock_data('KOTAKBANK', 'Kotak Mahindra Bank', 1820.00),
    generate_stock_data('LT', 'Larsen & Toubro Ltd', 3420.00),
    generate_stock_data('ASIANPAINT', 'Asian Paints Limited', 3180.00),
]

def get_stock_data() -> List[StockData]:
    """Return the list of stock data."""
    return stocks_data

def get_stock_by_symbol(symbol: str) -> StockData:
    """Get stock data for a specific symbol."""
    symbol_lower = symbol.lower()
    for stock in stocks_data:
        if stock['id'] == symbol_lower or stock['symbol'].lower() == symbol_lower:
            return stock
    raise ValueError(f"Stock with symbol {symbol} not found")