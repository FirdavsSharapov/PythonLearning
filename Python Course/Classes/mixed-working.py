dlevel = 0  # manage nesting level


def main():
    r = range(11)
    l = [1, 'two', 3, {'4': 'four'}, 5]
    t = ('one', 'two', None, 'Four', 'Five')
    s = set("It's a bird! It's a plane! It's Superman")
    d = dict(one=r, two=l, three=s)
    mixed = [l, r, s, d, t]
    disp(mixed)


def disp(x):
    print(x)
