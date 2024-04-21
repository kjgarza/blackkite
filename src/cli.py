# cli.py
import click

from commands import IngestDataCommand


@click.group()
def cli():
    """Command Line Interface for Data Ingestion System."""
    pass


@cli.command()
@click.argument("filename")
def ingest(filename):
    """Ingests data from the specified file."""
    command = IngestDataCommand(filename)
    command.execute()


if __name__ == "__main__":
    cli()
