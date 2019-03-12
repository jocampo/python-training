words = "This should be a list, yes?"

split_stuff = words.split()

#  Comprehension to iterate the list and only select the words with length of 4
print(' '.join([word for word in split_stuff if len(word) == 4]))
