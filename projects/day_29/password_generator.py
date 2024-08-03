import random


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_symbols = random.randint(2, 4)
    number_of_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(number_of_letters)]
    password_symbols = [random.choice(symbols) for _ in range(number_of_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(number_of_numbers)]

    password = password_letters + password_symbols + password_numbers

    random.shuffle(password)
    password = ''.join(password)

    return password
