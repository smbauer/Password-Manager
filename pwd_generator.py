from random import randint, choice, shuffle


def generate_password():
    '''Generate a random password with 8-10 letters, 2-4 numbers and 2-4 symbols'''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # randomly choose number of letters, numbers and symbols
    nr_letters= randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    
    letter_list = [choice(letters) for _ in range(nr_letters)]
    number_list = [choice(numbers) for _ in range(nr_numbers)]
    symbol_list = [choice(symbols) for _ in range(nr_symbols)]

    pwd_list = letter_list + number_list + symbol_list

    shuffle(pwd_list)
    return ''.join(pwd_list)
