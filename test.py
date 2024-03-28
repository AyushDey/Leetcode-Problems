numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filtering even numbers using Function 
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)

words = ['cat', 'dog', 'elephant', 'ant', 'bee', 'cow']
# Sort based on length and lexicographically
def length(w): 
    return (len(w),w) #tuple of length and word

words.sort(key= length)
print(words)
words.sort(key= lambda w: (len(w),w)) 
print(words)
#Sort a dictionary using values
