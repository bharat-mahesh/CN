from math import ceil, log
from tokenize import String

ip=input("Ip ")

def tobin(type):
    return '.'.join([bin(int(x)+256)[3:] for x in type.split('.')])

bip=tobin(ip)


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

print(addlist)

bitlist=list()
for x in addlist:
   bitlist.append(ceil(log(x,2)))

print(bitlist)
# print(sum(bitlist))
final=0

for i in range(len(bitlist)):
    def conv(ipsub,bitlist,i):
        count=32-bitlist[i]
        c=ipsub.replace('.','')
        x=[*c]
        l1=x[count:]
        l2=list()
        for a in range(len(l1)):
            l2.append(int(l1[a]))
        return l2

    c=bip.replace('.','')
    x=[*c]

    x1=conv(bip,bitlist,i)
    x2=conv(bsub,bitlist,i)

    l6=list()

    for p in x2:
        if(p==0):
            l6.append(1)
        else:
            l6.append(0)

    l7=list()

    for m,n in zip(x1,l6):
        l7.append(m|n)

    l5=list()
    for f,b in zip(x1,x2):
        l5.append(f&b)

    def tostr(lx,bitlist,i):
        count=32-bitlist[i]
        x10=list(map(str,lx))
        finalbip=x[:count]+x10
        str1=""
        str2=str1.join(finalbip)
        return str2

    p1=tostr(l5,bitlist,i)
    p2=tostr(l7,bitlist,i)

    def dispIP(stra):
        return ('.'.join(str(int(stra[i:i+8], 2)) for i in range(0, 32, 8)))

    print("First IP of subnet "+str(i+1)+" is: ")
    pbin1=p1[24:]
    pinteger=p1[16:24]
    finalp=(int(pinteger,2))
    pint1=int(pbin1,2)
    pint1str=str(pint1)
    op=dispIP(p1)
    fop=(op.replace(op[-1],str(final),1))
    arr=(fop.split('.'))
    # print(arr)
    # temp=arr[2]
    # arr[2]=arr[3]
    # arr[3]=temp

    if(int(arr[3])>255):
        arr[3]=str(int(arr[3])-255)
        arr[2]=str(int(arr[2])+1)
    print(".".join(arr))

    pbin=p2[24:]
    pint=int(pbin,2)
    pintstr=str(pint)
    final+=pint+1
    # if(final>255):
    #     final=final-255
    #     p1bin=p2[16:24]
    #     p1int=int(p1bin,2)
    #     p2.replace(str(p1int),str(p1int+1))
    print("Last IP of subnet "+str(i+1)+" is: ")
    
    op2=dispIP(p2)
    res=(final-256)
    print(res)
    if(res>=256):
        # print(pint1str)
        bruh=(op2.replace(pintstr,str(res-1)))
        list=bruh.split('.')
        list[2]=str(int(list[2])+1)
        print(".".join(list))

    else:
        print(op2.replace(pintstr,str(final-1)))

   