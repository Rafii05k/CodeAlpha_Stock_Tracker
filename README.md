# Stock Investment Tracker

## Overview

The Stock Investment Tracker is a Python-based tool designed to help you monitor and manage your stock investments. It provides real-time stock data, tracks your portfolio performance, and offers alerts for significant price changes.

## Features

- **Real-time Stock Data**: Fetches the latest stock prices from reliable financial APIs.
- **Portfolio Management**: Keeps track of your investments, including purchases and sales.
- **Performance Analysis**: Visualizes portfolio performance and historical data.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/stock-investment-tracker.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd stock-investment-tracker
    ```
3. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **API Keys**: Obtain API keys from financial data providers and add them to the `config.json` file. Example:
    ```json
    {
        "api_key": "YOUR_API_KEY"
    }
    ```
2. **Stock Symbols**: Configure your stock symbols and investment details in the `portfolio.csv` file.

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```
2. **Interact with the CLI or UI** (if applicable) to manage and view your stock investments.

## Contributing

Feel free to open issues, submit pull requests, or suggest improvements. For detailed contributing guidelines, refer to `CONTRIBUTING.md`.


## Contact

For any questions or feedback, please contact rafiakedir22@gmail.com

