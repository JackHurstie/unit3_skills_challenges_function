def grammar_checker(text):
    sentence_ending = ["!", ".", "?", "‽"]
    if text == "":
        raise Exception("We cannot test an empty string")
    if text[0] == text[0].upper() and text[-1] in sentence_ending:
        return True
    else:
        return False

