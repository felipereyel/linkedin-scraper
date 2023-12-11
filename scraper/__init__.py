from .driver import scraper
from .files import read_input, write_output


def scraper(i="input.csv", o="output.csv"):
    inputs = read_input(i)
    outputs = scraper(inputs)
    write_output(o, outputs)
