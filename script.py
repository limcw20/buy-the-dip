import typer
from utils.logic import check_stock_movement


app = typer.Typer()


#scan for specific ticker
@app.command()
def scan(ticker: str = typer.Argument(None, help="Enter the stock ticker symbol.")):
    if not ticker:
        ticker = typer.prompt("Which ticker do you want to scan?")
    typer.echo(f"🚀 Starting scan for {ticker.upper()}...")
    check_stock_movement(ticker)

if __name__ == "__main__":
    app()