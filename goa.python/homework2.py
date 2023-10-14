user_age = int(input("enter the users age: "))
user_gender = input("enter the users gender (male/female): ")
if (user_gender =="male" and user_age > 65) or (user_gender =="female" and user_age > 60):
    print("do you have a pension?")