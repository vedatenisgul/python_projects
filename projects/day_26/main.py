import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input("Enter a word: ").upper()
result = [alphabet[letter] for letter in user_input]
print(result)
