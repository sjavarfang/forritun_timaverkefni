while True:
    answer = input("You need something doubled? (Y)es? \n")
    if answer != "Y":
        break
    
    number = float(input("All right, then. Give me a number, and I'll double it for ya: \n"))
    d = number * 2
    print(d)
    
    while True:
        answer = input("You need something else doubled? (Y)es? \n")
        if answer != "Y":
            break
        number = float(input("All right, then. Give me a number, and I'll double it for ya: \n"))
        d = number * 2
        print(d)
    break