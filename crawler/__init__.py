from .driver import scraper
from .files import read_input, write_output


def crawler(i="input.csv", o="output.csv"):
    inputs = read_input(i)
    outputs = scraper(inputs)
    write_output(o, outputs)
