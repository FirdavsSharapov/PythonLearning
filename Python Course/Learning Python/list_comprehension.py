# You can have list comprehension by having write like this
# new_list = [new_item for item in list if condition]
new_array  = [
    1,
    2,
    3,
    5,
    6,
    7
]
new_list = [item for item in new_array if item > 4]
print(new_list) 

try:
    m = int(input("How many days for temperature reading? "))
except ValueError:
    print('This is not a number')


if(m>0):
    sum = 0
    for i in range(m):
        sum = sum + int(input("please input temprerature for day "))
    print(sum/m)
else:
    print("days are below 0 days")


myList2D= [[1,2,3],[4,5,6],[7,8,9]]
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum = sum + int(matrix[i][i])
    return sum

print(diagonal_sum(myList2D))