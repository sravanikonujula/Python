import numpy as np
#gives the random numbers with size 15
vec=np.random.random_integers(20,size=(15))
print("Vector with random integers :")
print(vec)
print("Most frequent value in the vector is :")
#helps to print the most frequent number
print(np.bincount(vec).argmax())