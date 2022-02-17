import typer
import lovesay.lovesay as lovesay

app = typer.Typer(add_completion=False)

@app.command()
def love():
    lovesay.main()

def main():
    app()
