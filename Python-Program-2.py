# With a single integer as the input, generate the following untill a = x
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n = int(input("please enter value:"))
for i in range(1,n):
    if i > 1:
        for j in range(1,i):
            if (i%j) == 0:
                print("input a=",i,"then output", j ,end=' ')
    print()
