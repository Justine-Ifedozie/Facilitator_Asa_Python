def take_in_a_word(word):
    dict = {}
    for letter in word:
        dict[letter] = dict.get(letter, 0) + 1
    print(dict)

take_in_a_word("google")

