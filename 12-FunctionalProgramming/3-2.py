text = 'I completely agree with you'
text = text.split()
no_letters = list(map(lambda x: len(x), text))

print(no_letters)