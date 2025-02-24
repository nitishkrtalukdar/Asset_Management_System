from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API Key
API_KEY = "YOUR_API_KEY"

def fetch_price(asset_name, asset_type):
    """Fetches the current market price of the asset."""
    if asset_type in ["stock", "forex"]:
        try:
            ts = TimeSeries(key=API_KEY)
            data, _ = ts.get_quote_endpoint(symbol=asset_name)
            return float(data["05. price"])
        except:
            return "Invalid"
    return None
