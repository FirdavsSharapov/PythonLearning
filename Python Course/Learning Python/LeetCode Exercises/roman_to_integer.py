def roman_to_int(s):
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        output = 0
        i = len(s)-1
        
        while i >= 0:
            if symbols[s[i]] > symbols[s[i-1]] and i != 0:
                output += (symbols[s[i]]-symbols[s[i-1]])
                i -= 1
            else:
                output += symbols[s[i]]
            i -= 1
        return output

if __name__ == '__main__':
    assert roman_to_int('III') == 3
    assert roman_to_int('MCMXCIV') == 1994
    assert roman_to_int('IV') == 4





