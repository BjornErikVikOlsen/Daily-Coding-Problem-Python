for i in range (1,101):
    k = ""
    if (i%3 == 0):
        k +="Fizz"
    if (i%5 == 0):
        k +="Buzz"
    if (k == ""):    
        k = i
    print(k)