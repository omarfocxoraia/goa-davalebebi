# import random 

# kids_names = ["giorgi nozadze , nika kandelaki , alexx , mate jorbenadze , omar focxoraia , giorgi gurwkaia , giorgi bibilashvili , "]

# random_kids =["0:6"]
# random.sample(kids_names, 3)

# for kid in "randoom_kids" : 
#     if kid["0:6"] == "i":
#         print(kid, "does well")
#     else:
#         print(kid, "cool")
import random

kids_names = ["giorgi nozadze", "nika kandelaki", "alexx", "mate jorbenadze", "omar focxoraia", "giorgi gurwkaia", "giorgi bibilashvili"]

random_kids = random.sample(kids_names, 3)

for kid in random_kids:
    if kid[:6] == "giorgi":
        print(kid, "does well")
    else:
        print(kid, "cool")

