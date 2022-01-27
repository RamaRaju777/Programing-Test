# With a single integer as the input, generate the follwogin until a = x
#==============================================================================================================================================================================
n = int(input("please enter value:"))
for i in range(1,n):
    for j in range(0,i+1):
        if j % 2 != 0:
            print("input a=",i,"then output",j,end=' ')
        else:
             print( ' ',end='')
    print()
