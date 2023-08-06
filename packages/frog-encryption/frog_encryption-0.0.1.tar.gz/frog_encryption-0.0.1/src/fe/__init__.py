import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '?', ',', '.', '(',
           ')', '*', '&', '^', '%', '$', '#', '@', '_', '-', ';', ':', '"', "'", '\n', '~', '`', '[', ']', '{', '}',
           '\\', '|', '=', '+', '/']
num_of_letters = 68




def check_num(list, num):
    if num not in list:
        return [True, num]
    else:
        fixedNum = random.randint(1, num_of_letters)
        return check_num(list, fixedNum)


def generate_key():
    global num_of_letters
    key = []
    for i in range(num_of_letters):
        num = random.randint(1, num_of_letters)
        sNum = check_num(key, num)
        if sNum[0]:
            key.append(sNum[1])
    return key


def generate_encoded_letters(key):
    global letters, num_of_letters
    encoded_letters = []
    for letter in range(num_of_letters):
        encoded_letters.append(letters[int(key[letter]) - 1])
    return encoded_letters

def encode_text(key, text):
    encoded_letters = generate_encoded_letters(key)
    global letters, num_of_letters
    output = ''
    for letter in text:
        try:
            location = letters.index(letter.lower())
            output += encoded_letters[location]
        except ValueError:
            output += letter

    return output

def decode_text(key, text):
    encoded_letters = generate_encoded_letters(key)
    global letters
    output = ''
    for letter in text:
        try:
            location = encoded_letters.index(letter.lower())
            output += letters[location]
        except ValueError:
            output += letter

    return output

def encode_file(key, location):
    f = open(location, 'r')
    file_content = f.read()
    f.close()

    encoded_content = encode_text(key, str(file_content))

    w = open(location, 'w')
    w.write(encoded_content)
    w.close()


def decode_file(key, location):
    f = open(location, 'r')
    file_content = f.read()
    f.close()
    decoded_content = decode_text(key, str(file_content))

    w = open(location, 'w')
    w.write(decoded_content)
    w.close()

def generate_key_file(location):
    key = generate_key()
    with open(location, 'w') as f:
        for number in key:
            f.write('~' + str(number))

def read_key_file(location):
    with open(location, 'r') as f:
        file_key = f.read()
    key = file_key.split('~')
    del key[0]
    return key

