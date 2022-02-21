import typer
import lovesay.lovesay as lovesay

app = typer.Typer(add_completion=False)

@app.command()
def love(color: str = typer.Argument('catppuccin', help="The name of your preferred color scheme")):
    """
    Supported color schemes: catppuccin, dracula, nord, gruvbox, and onedark
    """
    lovesay.main(color)

def main():
    app()
