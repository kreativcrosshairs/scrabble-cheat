"""
This module takes a Scrabble rack as a command line argument and prints all
valid Scrabble words that can be constructed from that rack, along with
their Scrabble scores, sorted by score.

An example invocation and output:

$ python main.py ZAEFIEE
17 feeze
17 feaze
16 faze
15 fiz
15 fez
12 zee
12 zea
11 za
6 fie
6 fee
6 fae
5 if
5 fe
5 fa
5 ef
2 ee
2 ea
2 ai
2 ae
"""
import inspect
from typing import List

import logging

FILENAME = 'sowpods.txt'
URL = 'http://courses.cms.caltech.edu/cs11/material/advjava/lab1/sowpods.zip'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def log_error(frame, message: str):
    """
    A utility function to handle logging of all the errors in the module.
    :param frame:
    :param message: str -> The error message to be logged.
    :return: None
    """
    logger = logging.getLogger(inspect.getframeinfo(frame).function)
    logger.error(message)


def get_word_list(filename: str) -> List[str]:
    """
    Constructs a word list.

    Opens and reads the given filename.
    Creates a list where each element is a word from the file.
    Also strips the newlines off the words.
    :param filename: str -> The file to be opened
    :return: List[str] -> A lost containing all the words in the file.
    """
    try:
        with open(filename, 'r') as f:
            return [word.strip('\n') for word in f.readlines()]
    except FileNotFoundError:
        log_error(inspect.currentframe(), f'{filename} not found. {URL}')
        return []


def main():
    """
    The entry point of the script.
    :return: None
    """
    word_list = get_word_list(FILENAME)


if __name__ == '__main__':
    main()
