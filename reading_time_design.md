## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(text)
    # Parameters
    #   text: a string representing human-readable text
    # return:
    #   a float representing a reading time
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words
It will return a reading time of 1
"""

estimate_reading_time(".....200.....") 
=> 1.0

"""
Given a text of 400 words
It will return a reading time of 2
"""

estimate_reading_time(".....400.....")
=> 2.0

"""
Given a text of 300 words
It will return a reading time of 1.5
"""

estimate_reading_time(".....300.....")
=> 1.5

"""
Given an empty string
It will return an error
"""

estimate_reading_time("")
=> Raises error: "Can't estimate reading time for an empty text."