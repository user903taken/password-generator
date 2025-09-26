import secrets
import string
choice = input("Do you want to create your own password (y/n):)")
if choice == "y":
    user_password = input("Enter your password:")
    if len(user_password) < 8:
        print("password should not be less than 8 characters")
    elif  user_password.islower():
        print(" your password is too weak")
    elif  user_password.isdigits():
        print(" your password is too weak")
    else:
        print("Your password is:",user_password)
    
else:
    password_length = secrets.choice(range(8, 12))  

    password_suggestions = int(input("How many suggestions do you want:"))
    for p in range(password_suggestions):
        password_requirements = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits), secrets.choice(string.punctuation)]

        remaining_characters = [secrets.choice(string.ascii_letters + string.digits +string.punctuation) 
        for r in range(password_length - 4) ]

        password_list = password_requirements + remaining_characters

    

        password = ''.join(secrets.choice(password_list) for _ in range(len(password_list)))


        print(f"{p+1}.Suggested password is: {password}")