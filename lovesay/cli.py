import typer
import lovesay.lovesay as lovesay

app = typer.Typer(add_completion=False)

@app.command()
def love(color: str = typer.Argument('catppuccin', help="The name of your preferred color scheme")):
    """
    Supported color schemes: catppuccin, dracula, nord, gruvbox, onedark, tokyonight, rosepine, ayu, palenight, and gogh 
    """
    lovesay.main(color)

def main():
    app()
