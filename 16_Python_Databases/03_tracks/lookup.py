def lookup(d, text):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == text:
            found = True
    return None