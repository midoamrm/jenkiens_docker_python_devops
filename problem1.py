#big(o) n**2
l_input=["1818005553531","31415926535","314159265385","81234567895","51234567898","581234567898"]
def check_serial_number(l_input):
    l=[]
    serial_number_l=[]
    num_of_problem=0
    for i in range(0,len(l_input)):
        flag=0
        index=0
        for j in range(0,len(l_input[i])):
            if l_input[i][j]=="8":
                index=j
                flag=1
                break
        if flag==0:
            serial_number_l.append(0)
        else:
           str=l_input[i][index:]
           #print(str)
           #print(len(str))
           if len(str)>=11:
             serial_number_l.append(1)
           else:
             serial_number_l.append(0)
            
    print(serial_number_l)

check_serial_number(l_input)