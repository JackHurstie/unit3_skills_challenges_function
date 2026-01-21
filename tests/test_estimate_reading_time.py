from lib.estimate_reading_time import *
import pytest

"""
Given a text of 200 words
It will return a reading time of 1
"""

def test_estimate_reading_time_for_200():
    result = estimate_reading_time("word " * 200)
    assert result == 1.0

"""
Given a text of 400 words
It will return a reading time of 2
"""

def test_estimate_reading_time_for_400():
    result = estimate_reading_time("word " * 400)
    assert result == 2.0

"""
Given a text of 300 words
It will return a reading time of 1.5
"""

def test_estimate_reading_time_for_300():
    result = estimate_reading_time("word " * 300)
    assert result == 1.5

"""
Given an empty string
It will return an error
"""

def test_estimate_reading_time_for_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for an empty text."