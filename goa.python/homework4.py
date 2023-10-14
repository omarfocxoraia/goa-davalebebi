for i in range(1, 101):
    output =""
    if i %3 ==0:
        output +="goa"
    if i % 5 ==0:
        output +="goa11"
    if i % 15 ==0:
        output ="goa15"
    if output =="":
        output = i 
    print(output)