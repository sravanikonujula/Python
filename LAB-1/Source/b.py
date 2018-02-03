# Function to middle words
x = input("What is your input ")
print(x)
A = x.split(" ")
# k be the length of the sentence
k = len(A)
print ("Middle word is: \n")
# if k is even 2 middle words will be obtained
if (k % 2 == 0):
    print("[" + A[int(k / 2) - 1] + ", " + A[int(k / 2)] + "]")
# if k is odd
if (k % 2 == 1):
    print("[" + A[int((k - 1) / 2)] + "]")

# Function to longest words
print("Longest word is: \n")
def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print (longest_word)

word_list = x.split()
find_longest_word(word_list)

# Function to Reverse words
print("After Reversing words in a sentence is: \n")
def reverseWordSentence(x):
    # Spliting the Sentence into list of words.
    words = x.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)
    return newSentence
# Driver's Code
# Calling the reverseWordSentence
# Function to get the newSentence
print(reverseWordSentence(x))