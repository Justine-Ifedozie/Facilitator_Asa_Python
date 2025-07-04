months = {'January':1, 'February': 2, 'March': 3, 'April': 3}

months2 = {number: name for name, number in months.items()}
print(months2)


word = 'Apple'
dict = {}
for letter in word:
    dict[letter] = word.count(letter)
print(dict)
