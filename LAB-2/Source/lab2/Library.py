class Person1:
    def __init__(self, name, emailadd):
        self.name = name
        self.email = emailadd
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
class Student1(Person1):
    StudCnt = 0
    def __init__(self, name, emailadd, stud_id):
        Person1.__init__(self, name, emailadd)
        self.stud_id = stud_id
        Student1.StudCnt +=1
    def displayCount(self):
        print("Total no of Students:", Student1.StudCnt)
    def display(self):
        print("Student Details are :")
        Person1.display(self)
        print("Student Id: ",self.stud_id)
class Librarian1(Person1):
    StudentCount = 0
    def __init__(self, name, emailadd, empl_id):
        super().__init__(name, emailadd)
        self.employee_id = empl_id
    def display(self):
        print("Employee Details are:")
        Person1.display(self)
        print("Employee Id is: ",self.employee_id)
class Book1():
    def __init__(self, Bname, author, bk_id):
        self.book_name = Bname
        self.author = author
        self.book_id = bk_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)
class Borrow_Buk(Student1, Book1):
    def __init__(self, name, emailadd, stuid, bookname, author, book_id):
        Student1.__init__(self, name, emailadd, stuid)
        Book1.__init__(self, bookname, author, book_id)
    def display(self):
        print("Required Borrowed Book Details:")
        Student1.display(self)
        Book1.display(self)
records= []
records.append(Student1('akash', 'akash25@gmail.com', 1811))
records.append(Student1('asha', 'asha@yahoo.com', 2457))
records.append(Librarian1('sumanth', 'sumanth@gmail.com', 64576))
records.append(Librarian1('janu', 'jenny@yahoo.com', 33221))
records.append(Book1('3 Mistakes', 'Chetan', 5454))
records.append(Book1('R programming', 'James', 7890))
records.append(Borrow_Buk('akash', 'akash25@gmail.com', 1811, 'R programming', 'James', 7890))
for obj, item in enumerate(records):
    item.display()
    print("\n")
    if obj == len(records)-1:
        item.displayCount()