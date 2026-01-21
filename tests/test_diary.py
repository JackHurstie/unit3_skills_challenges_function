from lib.diary import * 

'''
enter a string as an argument 
returns the first five words with '...' at the end.
'''
def test_inputting_5_words_make_snippet():
    result = make_snippet("hi my name is Jack and I'm a software developer.")
    assert result == "hi my name is Jack ..."
    
'''
enter a string less than five words
returns the words with no '...' appended.
'''
def test_inputting_less_than_5_words_make_snippet():
    result = make_snippet("hi my name is")
    assert result == "hi my name is"

'''
inputting a string of 10 words
return the integer 10
'''
def test_inputting_10_words_count_words():
    result = count_words("hi my name is Jack and I'm a software developer.")
    assert result == 10