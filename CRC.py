print("---SENDER---")
dataword=input("Enter the dataword ")
datawordlist=[i for i in dataword]
# print(datawordlist)

key=input("Enter the keyword ")
keylist=[i for i in key]
# print(keylist)

i=0
while i<len(keylist)-1:
    datawordlist.append('0')
    i+=1
# print(datawordlist)


def division(datawordlist,keylist):
    div=[]
    div2=[]
    div3=[]
    for x in range(len(keylist)):
        div.append(datawordlist[x])
    for y,z in zip(keylist,div):
        div2.append(int(y))
        div3.append(int(z))
    
    
    m=0
    while m<len(datawordlist):
    
        res=[]
        if(div3[0]==div2[0]):
            for d in range(len(div2)-1):
                res.append(div3[d+1] ^ div2[d+1])
        else:
            for d in range(len(div2)-1):
                res.append(div3[d+1] ^ 0)
    
        if(len(keylist)+m>len(datawordlist)-1):
    
            break
        else:
            res.append(int(datawordlist[len(keylist)+m]))
        m+=1    
    
        div3=res
    
    rem=[str(x) for x in res]
    # print(rem)
    
    dword1=datawordlist[:len(datawordlist)-3]
    
    encodedDataword=dword1+rem
    return encodedDataword


encodedDataword=division(datawordlist,keylist)    
print("Encoded data word is:",''.join(encodedDataword))

print("---RECEIVER--")

dataword1=input("Enter the dataword ")
datawordlist1=[i for i in dataword1]
# print(datawordlist)


i=0
while i<len(keylist)-1:
    datawordlist1.append('0')
    i+=1
# print(datawordlist)

decodedDataword=division(datawordlist1,keylist)



Syndrome=''.join(decodedDataword[len(datawordlist1)-len(keylist)+1:])
print("Syndrome is:",Syndrome)
check=Syndrome.find('1')
if(check==-1):
    print("Data is unaltered")
else:
    print("Data has been altered")