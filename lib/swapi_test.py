import pytest
from swapi import Swapi
import time 

obj = Swapi("https://swapi-graphql.netlify.app/.netlify/functions/index/")


def test_connection():
    chars = obj.get_characters()
    assert chars != {}


def test_structure():
    chars = obj.get_characters()
    assert isinstance(chars, dict)
    assert isinstance(chars["allPeople"], dict)
    assert isinstance(chars["allPeople"]["people"], list)


def test_get_chars():
    chars = obj.get_characters()
    assert len(chars["allPeople"]["people"]) > 0


def test_get_films():
    chars = obj.get_characters()
    for char in chars["allPeople"]["people"]:
        films = obj.get_films(char["id"])
        time.sleep(0.5)  # let's not ddos
        assert len(films) > 0
