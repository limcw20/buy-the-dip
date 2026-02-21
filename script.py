import typer
import yfinance as yf

app = typer.Typer()

def check_dip(symbol: str):
    ticker = yf.Ticker(symbol)
    # retrieve historical data for __ period and at every __ interval
    hist = ticker.history(period="5d", interval="15m") # returns a dataframe
    # print(hist)
    
    if hist.empty:
        typer.echo(f"No data found for {symbol}")
        return

    price_now = hist['Close'].iloc[-1] # first closing price in df
    price_start = hist['Close'].iloc[0] # last closing price in df
    
    percent_change = ((price_now - price_start) / price_start) * 100
    if percent_change < 0:
        typer.echo(f"{symbol} dipped {percent_change:.2f}% over the last 5 days.")
    elif percent_change > 0:
        typer.echo(f"{symbol} rose {percent_change:.2f}% over the last 5 days.")
    else:
        typer.echo(f"{symbol} had no change over the last 5 days.")

#scan for specific ticker
@app.command()
def scan(ticker: str = typer.Option(...,prompt="Search Ticker", help="Enter the stock ticker symbol.")):
    typer.echo(f"🚀 Starting scan for {ticker}...")
    check_dip(ticker)

if __name__ == "__main__":
    app()