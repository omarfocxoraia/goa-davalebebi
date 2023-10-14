# Create a list of team members
team_members = ["giorgi nozadze", "nika kandelaki", "alexx", "mate jorbenadze", "omar focxoraia", "giorgi gurwkaia", "giorgi bibilashvili"]

supersia = []

for i in team_members:
    if i.lower().count("i") > 2:
        supersia.append(i.title())

for i in supersia:
    print(i)