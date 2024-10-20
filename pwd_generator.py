import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #8 letter, 4 symbol, 4 number = g^2jk8&P12sdfj!!
    nr_letters= 8
    nr_symbols = 4
    nr_numbers = 4

    pwd_list = []

    for _ in range(nr_letters):
        pwd_list.append(random.choice(letters))
    for _ in range(nr_symbols):
        pwd_list.append(random.choice(symbols))
    for _ in range(nr_numbers):
        pwd_list.append(random.choice(numbers))

    random.shuffle(pwd_list)
    return ''.join(pwd_list)