from tokenize import String

ip=input("Ip ")

def tobin(type):
    return '.'.join([bin(int(x)+256)[3:] for x in type.split('.')])

bip=tobin(ip)


if bip[0]=='0':
    print("Class A")
elif bip[0]=='1' and bip[1]=='0':
    print("Class B")

elif bip[0]=='1' and bip[1]=='1':
    print("Class C")

subnet=input("Subnet ")

bsub=tobin(subnet)

count=(bsub.count('1'))

def conv(ipsub):
    c=ipsub.replace('.','')
    x=[*c]
    l1=x[count:]
    l2=list()
    for a in range(len(l1)):
        l2.append(int(l1[a]))
    return l2

c=bip.replace('.','')
x=[*c]

x1=conv(bip)
x2=conv(bsub)

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

def tostr(lx):
    x10=list(map(str,lx))
    finalbip=x[:count]+x10
    str1=""
    str2=str1.join(finalbip)
    return str2

p1=tostr(l5)
p2=tostr(l7)

def dispIP(stra):
    return print('.'.join(str(int(stra[i:i+8], 2)) for i in range(0, 32, 8)))

print("First IP is: ")
dispIP(p1)

print("Last IP is: ")
dispIP(p2)