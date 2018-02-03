#list of students enrolled in python class
py=['sindu','shanu','puja','saketh','sarath','vamsi','sravani','Ratna']
#list of students enrolled in web class
web=['saidu','Ratna','abhi','shanu','vamsi','suhas','sindu']

#to print students common in both classes
#It is Used by sets Concept
#Intersection is to extract common people.
print('Common students in both courses are: ', set(py).intersection(set(web)))
#to print students Only in python class
#Difference is to find students in python but not in web
print('ONLY python students are: ', set(py).difference(set(web)))
#to print students Only in web class
#Difference is to find students in web but not in python
print('ONLY web students are: ', set(web).difference(set(py)))
#Union is to find students in both web and python
print('students are: ', set(py).union(set(web)))
#It is just the difference between union and intersection.
print('Not common students are: ', (set(py).union(set(web))).difference(set(py).intersection(set(web))))