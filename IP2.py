from math import ceil, log
from tokenize import String

ip=input("Ip ")

def tobin(type):
    return '.'.join([bin(int(x)+256)[3:] for x in type.split('.')])

bip=tobin(ip)

def conv(ipsub,sub):
    c=ipsub.replace('.','')
    x=[*c]
    l1=x[sub:]
    l2=list()
    for a in range(len(l1)):
        l2.append(int(l1[a]))
    return l2


def tostr(lx,sub):
    x10=list(map(str,lx))
    finalbip=x[:sub]+x10
    str1=""
    str2=str1.join(finalbip)
    return str2

def dispIP(stra):
    return ('.'.join(str(int(stra[i:i+8], 2)) for i in range(0, 32, 8)))


subnet=input("Subnet ")

bsub=tobin(subnet)

count=(bsub.count('1'))

print("/",count)

left=32-count

available_addresses=(pow(2,left))

print("Available addresses = ",available_addresses)
numblocks=int(input("Enter the number of blocks "))

addlist=list()
for x in range(numblocks):
    address= int(input("Enter the address of the block "))
    
    f=pow(2,ceil(log(address,2)))
    if f>available_addresses:
        addlist.append(pow(2,int(log(available_addresses,2))))
        print("Capacity exceeded: Less addresses provisioned")
        break
    else:
        addlist.append(f)
        available_addresses-=f
    if available_addresses<=0:
        print("Capacity exceeded: No addresses available")
        break
    else:
        print("Available addresses: ",available_addresses)

# print(addlist)

bitlist=list()
for x in addlist:
   bitlist.append(ceil(log(x,2)))

# print(bitlist)

x1=conv(bip,count)
x2=conv(bsub,count)

c=bip.replace('.','')
x=[*c]
l5=list()
for f,b in zip(x1,x2):
    l5.append(f&b)

p1=tostr(l5,count)


firstip=[]

firstip.append(dispIP(p1))

lastip=[]
c=0
for i in addlist:
    # print(firstip)
    fip=firstip[c]
    arr=fip.split('.')
    x=int(arr[3])
    last=x+i
    arr[3]=str(last)
    if(int(arr[3])>=256):
        arr[2]=str(int(arr[2])+1)
        arr[3]=str(int(arr[3])-last)
    x=('.'.join(arr))
    firstip.append(x)
    


    c+=1
    
for i in firstip[1:]:
    li=i.split('.')
    y=int(li[3])
    last1=y-1
    if(last1<0):
        li[2]=str(int(li[2])-1)
        li[3]="255"
    else:
        li[3]=str(last1)
    p=('.'.join(li))
    lastip.append(p)

rem=(firstip[len(bitlist)])
firstip.remove(rem)

for i in range(len(firstip)):
    print("For subnet "+str((i+1)))
    print("First IP",firstip[i])
    print("Last IP",lastip[i])