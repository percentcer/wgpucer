import click
import subprocess

@click.group()
def cli():
    pass

# ------ WASM stuff -----------------------------------------------------------
# -----------------------------------------------------------------------------

@cli.group()
def wasm():
    """[module, web]"""
    pass

@wasm.command()
def module():
    """Build wasm-pack"""
    try:
        subprocess.run(['wasm-pack', 'build'], check=True)
    except Exception as e:
        click.echo(f"An error occurred while building wasm-pack: {e}")
@wasm.command()
def web():
    """Build wasm-pack for web"""
    try:
        subprocess.run(['wasm-pack', 'build', '--target', 'web'], check=True)
    except Exception as e:
        click.echo(f"An error occurred while building wasm-pack: {e}")

# ------ Serving --------------------------------------------------------------
# -----------------------------------------------------------------------------

@cli.command()
def serve():
    """Serve current dir over http"""
    try:
        subprocess.run(['npx','http-server','.'], check=True)
    except Exception as e:
        click.echo(f"Error while starting the HTTP server! {e}")

if __name__ == "__main__":
    cli()
