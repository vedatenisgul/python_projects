alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

def ceaser(input_text,shift_amount,direction):
    final_text =""
    if direction == "encode":
        shift_amount *= -1
    for letter in input_text:
        if letter not in alphabet:
            final_text+= letter
            continue
        position = alphabet.index(letter)
        final_position = ((position + shift_amount) % 26)
        final_text +=alphabet[final_position]
    print(f"The {direction}d text is {final_text}")

continue_process ="yes"
while (continue_process == "yes"):
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(input_text=text,shift_amount=shift,direction=direction)
    continue_process = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Good bye!")
 


