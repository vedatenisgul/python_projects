invited_names = []
letter_text = ""
PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    for name in names:
        new_name = name.replace(__old="\n", __new="")
        invited_names.append(new_name)

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_text = letter_file.read()

for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        inside_letter = letter_text.replace(__old=PLACE_HOLDER, __new=name)
        file.write(inside_letter)


