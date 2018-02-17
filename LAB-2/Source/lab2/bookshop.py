#List with Book names
B={"python":50,"web":30,"c":20,"java":40}
result=[]
#Give the minimum range
Min=int(input("Minimum price : "))
#Give the maximum range
Max=int(input("Maximum price: "))
for book,price in B.items():
    #this if function helps to print the result
    if price >= Min and price <= Max:
        result.append(book)
S=','.join(result)
print("Go with these  ("+S+")")