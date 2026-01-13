import requests

def get_crypto_price(symbol="BTC"):
    """Gets the current price of a cryptocurrency in USD."""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
        response = requests.get(url)
        data = response.json()
        price = float(data['price'])
        return f"The current price of {symbol} is ${price:,.2f}"
    except Exception as e:
        return "I'm sorry, I couldn't fetch the price right now."

# This list tells the "Brain" what tools are available
AVAILABLE_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_crypto_price",
            "description": "Get the current price of a cryptocurrency like BTC or ETH",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string", "description": "The coin symbol, e.g. BTC"}
                },
                "required": ["symbol"]
            }
        }
    }
]
