## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python

def grammar_checker(text):
    """checks for capital letter at text[0] and suitable sentence ending punctuation mark at text[-1].

    Parameters: (a sentence/ string of text)

    Returns: (True or False)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a sentence with capital at the beginning and exclamation mark at the end.
It returns True
"""
grammar_checker("Hello world!") => True

"""
Given a sentence with capital at the beginning and a comma at the end.
It returns False
"""
grammar_checker("Hello world,") => False

"""
Given a sentence with no capital at the beginning and a comma at the end.
It returns False
"""
grammar_checker("hello world") => False

"""
Given a sentence with no capital at the beginning and a full stop at the end.
It returns False
"""
grammar_checker("hello world.") => False

"""
Given an empty string.
It returns error
"""
grammar_checker("") => raises error: "We cannot test an empty string"

"""
Given just a capital letter and appropriate ending punction.
It returns True
"""
grammar_checker("U.") => True