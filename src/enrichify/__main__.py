"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Enrichify."""


if __name__ == "__main__":
    main(prog_name="enrichify")  # pragma: no cover
