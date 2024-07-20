from flask import Flask, request, render_template, redirect, url_for
import requests
import os
app = Flask(__name__)

portfolio = []

@app.route('/')
def index():
    return render_template('index.html', portfolio=portfolio)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    stock = request.form.get('stock')
    if stock and stock not in portfolio:
        portfolio.append(stock)
    return redirect(url_for('index'))

@app.route('/remove_stock', methods=['POST'])
def remove_stock():
    stock = request.form.get('stock')
    if stock in portfolio:
        portfolio.remove(stock)
    return redirect(url_for('index'))

@app.route('/track_portfolio', methods=['GET'])
def track_portfolio():
    stock_data = []
    for stock in portfolio:
        data = get_stock_data(stock)
        stock_data.append(data)
    return render_template('portfolio.html', stock_data=stock_data)


def get_stock_data(stock):
    api_key = os.getenv('API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'Time Series (1min)' in data:
        time_series = data['Time Series (1min)']
        latest_time = sorted(time_series.keys())[0]
        stock_info = {
            'symbol': stock,
            'time': latest_time,
            'open': time_series[latest_time]['1. open'],
            'high': time_series[latest_time]['2. high'],
            'low': time_series[latest_time]['3. low'],
            'close': time_series[latest_time]['4. close'],
            'volume': time_series[latest_time]['5. volume']
        }
    else:
        stock_info = {'symbol': stock, 'error': 'Data not available'}

    return stock_info


if __name__ == '__main__':
    app.run(debug=True)
