def multiplication_table(n):
    i=1
    while i<=10:
       t = n * i
       print(n,"*",i,"=",t) 
       i=i+1   


n = int(input("Enter the value :" ))

multiplication_table(n)