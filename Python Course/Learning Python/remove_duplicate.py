from datetime import date, timedelta


def count_digits(text: str) -> int:
    count = 0
    for char in text:
        if char.isnumeric():
            count += 1
    return count


# def days_diff(a, b):
#     start_date = date(*a)
#     end_date = date(*b)
#     return timedelta(end_date - start_date)

# print(days_diff((1982, 4, 19), (1982, 4, 22)))


def backward_string_by_word(text: str) -> str:
    words = text.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    new_words = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    new_sentence = " ".join(new_words)

    return new_sentence


print(backward_string_by_word('Hello  world'))

if __name__ == '__main__':
    print("Example:")
    print(count_digits('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
