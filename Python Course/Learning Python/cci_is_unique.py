# Question: Implement  an algorthm that determines if string has unique caracters

#  brute force solution O(n^2)
def uniqueu_string(string_value):
    for i in range(len(string_value)):
        for j in range (i+1, len(string_value)):
            if string_value[i] == string_value[j]:
                return True
            else:
                j+=1
    return False

# Optimized solution by using hash table
#  Space and time complexity is O(n)
# two questions here
#  1. Do  we count space as well or 
# def unique_string2(string_value):
#     string_holder = {}
#     for i in string_value:
#         if i in string_holder:
#             return True
#         else:
#             string_holder[i] = i
#     return False
    


# example_data = 'Hehlo Im your friend'

# unique_string2(example_data)


def isUniqueChars(st):

	# String length cannot be more than
	# 256.
	if len(st) > 256:
		return False

	# Initialize occurrences of all characters
	char_set = [False] * 128

	# For every character, check if it exists
	# in char_set
	for i in range(0, len(st)):

		# Find ASCII value and check if it
		# exists in set.
		val = ord(st[i])
		if char_set[val]:
			return False

		char_set[val] = True

	return True

# driver code
st = "abcd s q"
print(isUniqueChars(st))
