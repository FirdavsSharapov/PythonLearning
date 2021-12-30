def rotationalCipher(input, rotation_factor):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    new_word = ""
    for i in input:
        if i.isnumeric():
            num_char = numbers.find(i)
            if num_char > 0:
                new_word += numbers[(num_char+rotation_factor)%10]
            else:
                new_word += i
        else:
            char_at = characters.find(i)
            if char_at > 0:
                new_word += characters[((char_at-rotation_factor)%52)]
            else:
                new_word += i

    return new_word

if __name__ == '__main__':
    assert rotationalCipher('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39) == 'nopqrstuvwxyzABCDEFGHIJKLM9012345678'
