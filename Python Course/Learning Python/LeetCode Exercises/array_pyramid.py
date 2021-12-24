def valid_montain_array(arr):
    arr_len = len(arr)
    # False if len of the array less than 2 and last value is bigger than 
    # previous one
    if arr_len < 2 or arr[-1] >= arr[-2]:
        return False
    # Walk up
    i=0
    while arr[i] < arr[i+1] and arr[i] != arr[i+1]:
        i += 1

    while i < arr_len:
        if arr[i] > arr[i+1] and arr[i] != arr[i+1]:
            i += 1
        else: 
            return False
    return True

        
arra = [1,2,3,4,5,4,3,4,3]
print (valid_montain_array(arra))






    # # i = 1
    # arr_len = len(arr)
    # if arr_len < 2 or arr[-1] > arr[-2]:
    #     return False
    # for i in range(arr_len-1):
    #     if  arr[i] < arr[i+1] and arr[i] != arr[i+1]:
    #         i += 1
    #     elif arr[i] > arr[i+1] and arr[i] != arr[i+1]:
    #         i += 1
    #     else: 
    #         return False
    # return True

