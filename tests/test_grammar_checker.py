from lib.grammar_checker import *
import pytest

"""
Given a sentence with capital at the beginning and exclamation mark at the end.
It returns True
"""
def test_valid_sentence_grammar_checker():
    result = grammar_checker("Hello world!")
    assert result == True

"""
Given a sentence with capital at the beginning and a comma at the end.
It returns False
"""
def test_capital_but_wrong_end_grammar_checker():
    result = grammar_checker("Hello world,")
    assert result == False

"""
Given a sentence with no capital at the beginning and a comma at the end.
It returns False
"""
def test_no_capital_and_no_grammar_checker():
    result = grammar_checker("hello world")
    assert result == False

"""
Given a sentence with no capital at the beginning and a full stop at the end.
It returns False
"""
def test_no_capital_but_valid_end_grammar_checker():
    result = grammar_checker("hello world.")
    assert result == False

"""
Given an empty string.
It returns False
"""
def test_empty_string_grammar_checker():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    error_message = str(e.value)
    assert error_message == "We cannot test an empty string"

def test_minimum_value_grammar_checker():
    result = grammar_checker("U.")
    assert result == True