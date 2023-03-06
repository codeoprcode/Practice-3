
while 8 == 8:

    num_1 = int(input("Please enter first Number= "))
    num_2 = int(input("Please enter first Number= "))
    devisor_final1=[]
    devisor_final2=[]
    devisor_common=[]


        
    if int(num_1) == num_1 and int(num_2) == num_2:

        for i in range(1, (num_1)+1):

            devisor_1 = num_1/i
            if int(devisor_1) == devisor_1:
                devisor_final1.append(devisor_1)


        for j in range(1, (num_2)+1):

            devisor_2 = num_2/j
            if int(devisor_2) == devisor_2:
                devisor_final2.append(devisor_2)


        for k in range(len(devisor_final1)):
            if devisor_final1[k] in devisor_final2:
                devisor_common.append(devisor_final1[k])
                
        gcd = devisor_common[0]
        
        lcm = abs(num_1) * abs(num_2) / gcd

        print(lcm)

        
    else:
        print("Please Enter Integer Number")

