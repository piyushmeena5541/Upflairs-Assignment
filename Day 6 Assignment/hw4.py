def right_triangle_pattern(n):
    row = 1
    while row <= n:
        col = 1
        while col <= row:
            print("*",end="")
            col+=1

        print()
        row+=1
        
n = int(input("Enter the number of rows :" ))
right_triangle_pattern(n)       