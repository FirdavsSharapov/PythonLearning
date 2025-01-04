data = [2,4,6,8,10,12,14,16,17,18,19,20,22,24,25]
target = 25

def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def benary_search_itterative(data, target):
    start = 0
    end  = len(data) - 1 # -1 because array starts with 0 element
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == target:
            print(data[middle])
            return True
        elif data[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return False 

print(benary_search_itterative(data, target))