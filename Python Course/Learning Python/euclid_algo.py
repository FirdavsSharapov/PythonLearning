def gdc_algo(x,y) -> int:
    while y != 0:
        t_value = y
        y = x % y
        x = t_value
    return x

print (gdc_algo(15,15654))
