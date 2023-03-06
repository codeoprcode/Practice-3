import random


n = int(input("Please Enter a Arrey Length= "))
m = int(input("Please Enter Positive Number for Range End= "))
list=[]


if m < n:
    print("Range End must be greater than Array Length")

else:

    for i in range(n):
        x = random.randint(1, m)

        if x in list:
            y = random.randint(1, m)
            list.append(y)

        else:
            list.append(x)

    print(list)