from textblob import TextBlob

def spelling_checker():
    while True:
        word = input('Enter a word : ')
        # checking if the input word is correct
        if word != TextBlob(word).correct():
            # suggesting the correct word to the user
            question = input(f'Did you mean '
                            f'{TextBlob(word).correct()}?. '
                            f'type yes/no :')
            if question == 'yes':
                break
            else:
                print('Please try again')
        # if the word entered is correct
        # the code breaks and returns word
        elif word == TextBlob(word).correct():
            break
    return f'Your word is, {TextBlob(word).correct()}'

print(spelling_checker())