def sum_of_arguments(*args):
   sum_arg = 0
   len_args = len(args)
   for i in args:
       sum_arg = sum_arg + i
   print ("Mean of the args is: ", sum_arg/len_args)    
   return sum_arg

def list_of_words(*words):
    shortest = 0
    longest = 0
    avg_sum = 0
    for i in words:
        if shortest < len(i):
            shortest = len(i)
        elif longest < len(i):
            longest = len(i)
        avg_sum += len(i)
    return (shortest, longest, avg_sum/len(words))

print (sum_of_arguments(10,20,30,40))
print (list_of_words("sabaka", "dog", "cat", "porohod"))