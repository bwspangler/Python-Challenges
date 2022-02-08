
"""
 ord()function returns the ASCII (American Standard Code for Information Interchange).
 By using it and subtracting 96 - which represents the value before lowercase 'a', I am
 able to easy return the order value of the numbers, without creating a laborious function
 to parse out the respective values for each individual letter (at least 52 lines of code)
"""
def letter_value(letter):
    letterval = ord(letter)-96
    return letterval


"""
From that, we have a function which works through the word, going letter by letter for
Each letter in the word
"""
def word_value(word):
    wordval = 0
    for s in word:
        wordval += letter_value(s)
    return wordval


"""
This is our actual main() function and will run through the words listed to 
parse out their individual values and print them out
"""
s = ["", 'a', 'z', 'cab', 'excellent', 'microspectrophotometrics']


for word in s:
    print(word_value(word))
