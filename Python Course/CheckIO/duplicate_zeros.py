from array import array
def duplicate_zeros(donuts)-> list[int]:
    newArray = []
    lenDonuts = len(donuts)
    i=0
    j=0
    while(i<lenDonuts):
        newArray.insert(j, donuts[i])
        if(donuts[i] == 0):
            newArray.insert(j+1, 0)
            j+=2
        else:
            j+=1
        i+=1
            
    return newArray
    


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")