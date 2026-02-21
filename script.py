import typer
import yfinance as yf

app = typer.Typer()

def check_stock_movement(symbol: str):
    ticker = yf.Ticker(symbol)
    # retrieve historical data for __ period
    hist = ticker.history(period="5d") # returns a dataframe
    # print(hist)
    
    if hist.empty:
        typer.echo(f"No data found for {symbol}")
        return

    price_now = hist['Close'].iloc[-1] # first closing price in df
    price_start = hist['Close'].iloc[0] # last closing price in df
    
    percent_change = ((price_now - price_start) / price_start) * 100
    if percent_change < 0:
        typer.echo(f"{symbol.upper()} dipped {percent_change:.2f}% over the last 5 trading days.")
    elif percent_change > 0:
        typer.echo(f"{symbol.upper()} rose {percent_change:.2f}% over the last 5 trading days.")
    else:
        typer.echo(f"{symbol.upper()} had no change over the last 5 trading days.")

#scan for specific ticker
@app.command()
def scan(ticker: str = typer.Argument(None, help="Enter the stock ticker symbol.")):
    if not ticker:
        ticker = typer.prompt("Which ticker do you want to scan?")
    typer.echo(f"🚀 Starting scan for {ticker.upper()}...")
    check_stock_movement(ticker)

if __name__ == "__main__":
    app()