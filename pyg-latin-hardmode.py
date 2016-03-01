ay_ending = "ay"
vowel_ending = "say"
raw_word = input("What word(s) would you like to be translated? ")
word_list = raw_word.lower().split(" ")  # split the sentence into a list


def translate(word_list):      # function for translating
    for untranslated_word in word_list:     # for every untranslated word in the word list, run...
        # translate function, translates the words from the list
        if untranslated_word[0] in "aeiou":
            ending = vowel_ending
        else:
            ending = untranslated_word[0] + ay_ending
        front = untranslated_word[1:]
        print("{}{}".format(front, ending), end=" ")

print("\n")
print("Here are your translated words:")
translate(word_list)
print("\n")