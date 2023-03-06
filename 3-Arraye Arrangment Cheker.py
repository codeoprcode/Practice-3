print("Hello Dear User")

user_entry = int(input("Please enter your entries number: "))
num_list = []


for i in range(user_entry):
    
    user_num = int(input("Please enter your numbers: "))
    num_list.append(user_num)

sorted_num_list = sorted(num_list)

if sorted_num_list == num_list:
    print("Your list is sorted. ✔")
else:
    print("Your list is not sorted. ❌")
    print("This is sorted: " , sorted(num_list))
