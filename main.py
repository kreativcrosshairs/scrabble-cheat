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
import argparse
import inspect
from typing import List

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

FILENAME = 'sowpods.txt'
URL = 'http://courses.cms.caltech.edu/cs11/material/advjava/lab1/sowpods.zip'

SCORES = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
          'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
          'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1,
          'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
          'x': 8, 'z': 10}


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


def get_rack() -> List[str]:
    """
    Extracts the rack from the command arguments
    :return: str -> A string representing the letters in the rack
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('rack')
    return list(parser.parse_args().rack.upper())


def get_valid_words(rack: List[str], word_list: List[str]) -> List[str]:
    """
    Gets a list of valid words that could be formed from the letters in the
    rack
    :param rack: List[str] -> A list containing letters
    :param word_list:  List[str] -> A list containing all the words
    :return: List[str] -> A list of valid words
    """
    valid_words = []
    for word in word_list:
        valid_word = True
        for letter in word:
            if word.count(letter) > rack.count(letter):
                valid_word = False
        if valid_word:
            valid_words.append(word)
    return valid_words


def get_word_score(word: str) -> int:
    """
    Returns the total score of the given word
    :param word: str
    :return: int
    """
    score = 0
    for letter in word.lower():
        score += SCORES[letter]
    return score


def display_scores(word_list: List[str]):
    """
    Sorts the words and displays the score for each word
    :param word_list: str
    :return: None
    """
    word_list = sorted(word_list, key=get_word_score, reverse=True)
    for word in word_list:
        print(f'{get_word_score(word)} - {word}')


def main():
    """
    The entry point of the script.
    :return: None
    """
    word_list = get_word_list(FILENAME)
    rack = get_rack()
    valid_words = get_valid_words(rack, word_list)
    display_scores(valid_words)


if __name__ == '__main__':
    main()
