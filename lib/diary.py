def make_snippet(string):
    if len(string.split()) > 5:
        first_five_words = string.split()[:5]
        result = ' '.join(first_five_words) + " ..."
    else:
        result = string
    return result


make_snippet("hi my name is Jack and I'm a software developer.")

def count_words(string):
    return len(string.split())