# cli.py
import click

from commands import IngestDataCommand, QueryDataCommand


@click.group()
def cli():
    """Command Line Interface for Data Ingestion System."""
    pass


@cli.command()
@click.argument("path")
def ingest(path: str) -> None:
    """Ingests data from the specified file."""
    command = IngestDataCommand(path)
    command.execute()


@cli.command()
@click.argument("query")
def query(query: str) -> None:
    """Queries the data store for the specified query."""
    command = QueryDataCommand(query)
    command.execute()


if __name__ == "__main__":
    cli()
