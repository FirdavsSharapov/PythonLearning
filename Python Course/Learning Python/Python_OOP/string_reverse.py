import stack_class

word = "Some, test, word"
reversed_words = ""
s = stack_class.Stack()

for char in word:
    temp = s.peek(word)
    reversed_words = s.push(temp)
    print(s)

print (reversed_words)
