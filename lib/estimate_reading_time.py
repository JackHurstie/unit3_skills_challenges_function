'''
two_hundred = "word " * 200
print(len(two_hundred.split()))
'''

def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for an empty text.")
    return len(text.split()) / 200