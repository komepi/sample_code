import click
import time
import os


@click.command()
@click.argument('count', type=int)
def countdown(count):

    numbers = range(count, -1, -1)
    with click.progressbar(numbers,show_pos=True) as bar:
        for num in bar:
            time.sleep(1)


if __name__ == '__main__':
    countdown()