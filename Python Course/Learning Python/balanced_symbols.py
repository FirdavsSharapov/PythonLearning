# class BalancedSymb:

#     def __init__(self):
#         self.items = []   
   
def check_symbols(symbols: str)-> bool:
    symbols_len = len(symbols)
    symbol_counter = 0
    if (symbols_len % 2) == 0:
         while symbol_counter < symbols_len:
            front_symbol = symbols[symbol_counter]
            back_symbol = [-1]
            if front_symbol == back_symbol:
                symbol_counter += 1
                return True
            else: 
                return False
    else:
        return False

if __name__ == '__main__':
    # These "asserts" using for self-checking and not for auto-testing
    assert check_symbols("[({::})]") == True

    assert check_symbols("({[})") == False

    print('Done! Looks like it is fine. Go and check it')