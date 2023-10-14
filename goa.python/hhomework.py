while True:
    user_age = int(input("Enter your age (-1 to quit): "))
    
    if user_age == -1:
        break
    
    for age in range(user_age + 1):
        if age == 8:
            print("You have entered Goa")
        else:
            print(f"Congratulations! You have become {age} year{'s' if age != 1 else ''} old")

