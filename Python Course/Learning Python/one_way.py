def oneEditAway(first, second):
    if len(first) == len(second):
        return oneEditReplace(first, second)
    elif len(first)+1 == len(second):
        return oneEditInsert(first, second)
    elif len(first)-1 == len(second):
        return oneEditInsert(first, second)
    else: 
        return False

def  oneEditReplace(fisrt, second):
    found_diff = False
    for i in range(len(fisrt)):
        if fisrt[i] != second[i]:
            if found_diff == True:
                return False
            found_diff = True
    return True

def oneEditInsert(first, second):
    index1 = 0
    index2 = 0
    len_second = len(second)
    while index2 < len_second  :
        if first[index1] != second[index2]:
            if index1 != index2:
                return False
            index2 +=1
        else:
            index1+=1
            index2+=1
    return True


print (oneEditAway("pale", "bae"))