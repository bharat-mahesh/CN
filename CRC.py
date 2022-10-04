dataword=input("Enter the dataword ")
datawordlist=[i for i in dataword]
# print(datawordlist)

key=input("Enter the keyword ")
keylist=[i for i in key]
# print(keylist)

i=0
while i<3:
    datawordlist.append('0')
    i+=1
# print(datawordlist)



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

print("Encoded data word is:",''.join(encodedDataword))