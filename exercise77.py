# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
# and, total characters (all letters and special characters minus
# whitespaces) in a string. Return everything in a dictionary format:

# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}

# Use the string below as an argument:

# “Python has a string format operator %. This functions
# analogously to printf format strings in C, e.g. "spam=%s
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".

def analyse_string(s):
    special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    dict = {}
    special_char = ""
    total_char_count = 0
    for i in s:
        if i in special_characters:
            special_char += i
    dict["special character"] = len(special_char)
    words = s.split(" ")
    dict["number"] = len(words)
    for word in words:
        total_char_count += len(word)
    dict["total characters"] = total_char_count
    print(dict)


text = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'."
analyse_string(text)