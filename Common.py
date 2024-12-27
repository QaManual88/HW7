def correct_sentence(sentence):
    if not sentence[0].isupper():
        sentence = sentence[0].upper() + sentence[1:]

    if not sentence.endswith('.'):
        sentence += '.'
    return sentence
print(correct_sentence("greetings, friends"))