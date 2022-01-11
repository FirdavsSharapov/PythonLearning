def recursive_factorial(num):
    assert num >= 0 and int(num) == num, 'The number must be positive integer only' 
    if num == 0 or num == 1:
        return 1
    else:
        return num * recursive_factorial(num-1)


print(recursive_factorial(-1))


# if __name__ == '__main__':
#     assert recursive_factorial(4) == 24