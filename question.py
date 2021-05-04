input1=[4,3,5]
input2="PNP"
input2=list(input2)
count=0
n=len(input1)
for i in range(n):
    if(input2[i]=="P"):
        count=count+input1[i]
    else:
        count=count-input1[i]
print(count*100)