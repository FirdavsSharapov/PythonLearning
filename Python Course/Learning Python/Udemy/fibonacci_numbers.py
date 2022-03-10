def fibonacci_numbers (num):
    assert ()
    if num <= 1:
        return num
    else:
        return fibonacci_numbers(num-1) + fibonacci_numbers(num-2)


print(fibonacci_numbers(-1))