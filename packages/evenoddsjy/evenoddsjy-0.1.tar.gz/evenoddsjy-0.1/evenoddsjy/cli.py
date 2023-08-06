"""A sample CLI."""

import click
import log

from . import utils


@click.command()
@click.argument('feet')
@click.argument('num1', type=int)
@click.argument('num2', type=int)
def main(feet: str, num1: int, num2: int):
    log.init()

    meters = utils.feet_to_meters(feet)

    sum1 = utils.add(num1, num2)

    click.echo(f'{feet} feet is {meters} meters.')

    click.echo(f'{num1} + {num2} = {sum1}')

    if meters is not None:
        click.echo(meters)


if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
