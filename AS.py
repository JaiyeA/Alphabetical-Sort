#Alphabetical sorting
#Only sorts by comparing the first letter of two words
import math

AlphaB = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}

def AlphabeticalMergeSort(m):
    #base case
    if len(m) <= 1:
        return m

    left = []
    right = []
    for i in range(len(m)):
        if i < math.floor(len(m)/2):
            left.append(m[i])
        else:
            right.append(m[i])
    #breaking up the arrays into individual arrays of one element
    left = AlphabeticalMergeSort(left)
    right = AlphabeticalMergeSort(right)
    #merging while also sorting the individual arrays. Eventually we end up with 2 sorted arrays that will, in turn, be merged into one final sorted array
    return Merge(left, right)

def Merge(left, right):
    result  = []
    while left and right:
        #searches dictionary for the number paired with the letter
        if AlphaB[left[0][0]] <= AlphaB[right[0][0]]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result

words = ['nerve','axon','terminal','vesicle','synapse','dendrite']
print(AlphabeticalMergeSort(words))
