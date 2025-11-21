def stripSpaces(text):
    stripped_text = ""
    for char in text:
        if char == " ":
            char = ""
        stripped_text = stripped_text + char
    return stripped_text

if __name__ == "__main__":
    text = "A programming language is a system of notation for writing computer programs"
    print(f'Tekst: {text}')
    print(f'Tekst bez spacji: {stripSpaces(text)}')