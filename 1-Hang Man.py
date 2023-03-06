import random

data_bank = ["blue bank", "baba bastani", "sib maz", "kotton", "giordano", "jeanwest", "brands"]

cpu_word = random.choice(data_bank)
user_mistakes = 0
correct_g = []
incorrect_g = []
x = len(cpu_word)

while user_mistakes < 8:

    for i in range(len(cpu_word)):
        
        if cpu_word[i] in correct_g:
            print(cpu_word[i], end=" ")

        else:
            print("-", end=" ")


    user_g = input("please enter your letter= ")
    user_gfinal = user_g.lower()
        
    if len(user_g) == 1:         
        if user_gfinal in cpu_word:
            print("✔")
            correct_g.append(user_gfinal)

        else:
            print("❌")
            user_mistakes +=1
            incorrect_g.append(user_gfinal)
    else:
        print("please type one letter")

    if len(set(cpu_word)) == len(correct_g):
        print("You Win 💥✔🔥")
        print(cpu_word, " 👌👌👌")
        break   
    



if user_mistakes == 8:
    print("game over 💤💤💤")


