import yfinance as yf

def get_fii_data(ticker):
    fii = yf.Ticker(f"{ticker}.SA")
    return {
        'preco': fii.history(period='1d')['Close'][0],
        'dividendos': fii.dividends
    }