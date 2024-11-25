# Write a function that has one parameter and takes a list of words
# as an argument. The function returns the longest word from the
# list. Name the function longest_word. The function should
# return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your
# function should return
# [10, JavaScript] as the longest word.

def longest_word(list):
    longest = ""
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
            longest = i
    print(f"[{len(longest) }, {longest}]")


words = ["Java", "JavaScript", "Python"]
longest_word(words)