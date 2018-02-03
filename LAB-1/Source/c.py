#if there is triplet continues with next step
# A[] the triplet be like
def Numbers(A, array_size, sum):
    # initial be A[i]
    for i in range(0, array_size - 2):

        # And the second be A[j]
        for j in range(i + 1, array_size - 1):

            # coming to third be A[k]
            for k in range(j + 1, array_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Wanted Triplet is", A[i],
                          ",", A[j], ",", A[k])
                    return True
    return False
A =[3, 3, 1, 2, -4, 0, 1]
sum = 0
array_size = len(A)
Numbers(A, array_size, sum)

