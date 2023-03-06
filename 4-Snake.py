print("🐍Snake🐍")

n = int(input("Enter the Snacke Length: "))

for i in range(n):
    if i % 2 == 0:
        print("*", end="")
    else:
        print("#", end="")
