#list with contacts and respective details
Contacts=[{"name":"Shanu","number":"0727","email":"coolshanu888@gmail.com"},{"name":"ramya","number":"8117","email":"ramyakonujula@gmail.com"},{"name":"Sravani","number":"8111","email":"sravanikonujula@gmail.com"}]
while True:
    #select an option
    print("1) Display contact by name")
    print("2) Display contact by number")
    print("3) Edit contact by name")
    print("4) Exit")
    # X takes the input for the option
    X=str(input("select the option: "))

    if X=='1':
        #User selects 1 this gets executed give respective details
        A=(input("Enter the name: "))
        print(next(item for item in Contacts if item["name"]==A))
    elif X=='2':
        #this goes with 2 gets executed give respective details
        B=(input("Enter the number: "))
        print(next(item for item in Contacts if item["number"]==B))
    elif X=='3':
        #Helps to edit the contact name.
        C=input("Select the contact which you want to edit: ")
        for item in Contacts:
            if item["name"]==C:
                item["number"]=input("Enter the new contact number: ")
        print(Contacts)
    elif X=='4':
        #this is to get out of it.
        break



