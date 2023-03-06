print("Word Counterrrr")

phrase = input("Please enter your phrase= ")
counter = 0

for i in range(len(phrase)):
    if phrase[i] == " ":
        counter += 1

print((counter+1))