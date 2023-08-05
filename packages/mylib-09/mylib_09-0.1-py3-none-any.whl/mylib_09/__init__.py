def pattern(string):
    n=len(string)
    print(n)
    for i in range(1,n+1):
        
        if i==1:
            print(string)
        else:
            for j in range(1,i): 
                print("_", end="")
            print(string[0:n-j])