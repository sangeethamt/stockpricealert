import requests
import smtplib
from email.mime.text import MIMEText

# Define the API endpoint and your API key
API_URL = "https://www.alphavantage.co/query"
API_KEY = "QDT3DZXP7IZRNXF4"

# Define the stock ticker and the threshold price
ticker = "MSFT"  # For Microsoft
threshold_price = 150.00

def get_stock_price(ticker):
    """
    Fetch the latest stock price for the given ticker symbol.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        float: The latest stock price.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "1min",
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    latest_time = list(data["Time Series (1min)"].keys())[0]
    latest_price = float(data["Time Series (1min)"][latest_time]["4. close"])
    return latest_price

def send_email_debug(price):
    """
    Send an email alert when the stock price reaches the threshold.

    Args:
        price (float): The current stock price.
    """
    sender = "your_email@example.com"
    receiver = "receiver_email@example.com"
    subject = f"Stock Price Alert: {ticker}"
    body = f"The stock price of {ticker} has reached ${price:.2f}."

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("localhost", 1025) as server:
        server.sendmail(sender, receiver, message)

def main():
    """
    Main function to fetch the stock price and send an alert if the price reaches the threshold.
    """
    price = get_stock_price(ticker)
    print(f"Current price of {ticker}: ${price:.2f}")

    if price >= threshold_price:
        send_email_debug(price)
        print(f"Alert sent! {ticker} has reached ${price:.2f}")

if __name__ == "__main__":
    main()


  