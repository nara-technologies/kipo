import typer

app = typer.Typer()

@app.command()
def version():
    """Show Kipo version"""
    print("Kipo v0.0.1")

@app.command()
def studio():
    """Launch Kipo Studio"""
    print("Kipo Studio coming soon")