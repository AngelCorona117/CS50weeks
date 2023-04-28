# TODO
from cs50 import get_string

text = get_string("Text: ")
# calculate number of characters
characters = len(text) - text.count(' ') - text.count('!') - text.count('.') - text.count('?')
# calculate number of words
words = text.count(" ")+1
# calculate number of sentences
sentences = text.count('!')+text.count('.')+text.count('?')
# get averange number of letters
L = round(characters / words * 100)
# get averange number of sentences
S = round(sentences / words * 100)
# calculate the grade
grade = 0.0588 * L - 0.296 * S - 15.8
# print grade
if grade < 1:
    print("Before  Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")