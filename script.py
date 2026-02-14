import typer

app = typer.Typer()

@app.command()
def scan():
    """
    This docstring becomes the help text in the terminal!
    """
    print("Testing...")

if __name__ == "__main__":
    app()