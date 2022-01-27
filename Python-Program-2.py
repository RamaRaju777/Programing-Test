#With a single integer as the input, generate the following untill a = x
#==================================================================================================================================================================================

for i in range(1,10):
    if i > 1:
        for j in range(1,i):
            if (i%j) == 0:
                print("input a=",i,"then output", j ,end=' ')
    print()
