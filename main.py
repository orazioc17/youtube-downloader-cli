import typer


app = typer.Typer()

    
@app.command()
def audio(url: str):
    """
    Downloads a youtube video and converts it to audio
    """
    print(url)


@app.command()
def video(url: str):
    """
    Downloads a youtube video
    """
    print(url)


if __name__ == '__main__':
    #typer.run(main)
    app()