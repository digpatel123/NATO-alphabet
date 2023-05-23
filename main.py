import pandas

#TODO 1. Create a dictionary in this format:

df = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input("Please enter a word or name for which you want the NATO alphabets: ").upper())

nato_codes = [alpha_dict[let] for let in user_input]

print(nato_codes)