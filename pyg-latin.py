ay_ending = "ay"
vowel_ending = "say"
raw_word = input("What word would you like to be translated? ")
word = raw_word.lower()
front = word[1:]
if word[0] in 'aeiou':
    ending = vowel_ending
else:
    ending = word[0] + ay_ending
print("{}{}".format(front, ending))