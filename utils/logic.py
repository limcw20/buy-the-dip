import yfinance as yf
import typer

def check_stock_movement(symbol: str):
    ticker = yf.Ticker(symbol)
    # retrieve historical data for __ period
    hist = ticker.history(period="5d") # returns a dataframe
    # print(hist)
    
    if hist.empty:
        typer.echo(f"No data found for {symbol}")
        return

    price_now = hist['Close'].iloc[-1] # latest price in df
    price_start = hist['Close'].iloc[0] # oldest price in df
    
    percent_change = ((price_now - price_start) / price_start) * 100
    if percent_change < 0:
        typer.echo(f"{symbol.upper()} dipped {percent_change:.2f}% over the last 5 trading days.")
    elif percent_change > 0:
        typer.echo(f"{symbol.upper()} rose {percent_change:.2f}% over the last 5 trading days.")
    else:
        typer.echo(f"{symbol.upper()} had no change over the last 5 trading days.")