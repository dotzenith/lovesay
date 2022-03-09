from typing import Optional
import typer
import lovesay.love as lovesay

app = typer.Typer(add_completion=False)

@app.command()
def love(
    quote: Optional[str] = typer.Argument(None, help="An arbitrary message to print", show_default=False), 
    color: str = typer.Option('catppuccin', "--color", "-c", help="The name of your preferred color scheme")        
):
    """
    Supported color schemes: catppuccin, dracula, nord, gruvbox, onedark, tokyonight, rosepine, ayu, palenight, and gogh 
    """
    lovesay.main(quote, color)

def main():
    app()
