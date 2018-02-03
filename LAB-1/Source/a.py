SpecialSym=['$','@','#','!']
while True:
 password= input("create your password :")
 if len(password)< 6:
     print("your password requires at least 6 char length")
     continue
 elif len(password)> 16 :
     print("your password should not exceed 16")
     continue
 elif not any(char.isdigit() for char in password):
     print('your password requires at least one numeral')
     continue
 elif not any(char.isupper() for char in password):
     print('your password requires at least one Uppercase letter')
     continue
 elif not any(char.islower() for char in password):
     print('your password requires at least one Lowercase letter')
     continue
 elif not any(char in SpecialSym for char in password):
     print('your password should contain one of the mentioned symbols $@#!')
     continue
 else :
     print("The password you entered is correct")
     print(password)
     break
