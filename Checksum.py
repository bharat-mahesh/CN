import textwrap

def hexConvert(inp_str):
    inp_arr=[x for x in inp_str]

    hex_arr=[]
    for i in inp_arr:
        hex_char=(hex(ord(i)))
        hex_arr.append(hex_char[2:])


    nums=''.join(hex_arr)
    
    if len(nums)%4 !=0:
        nums+='00'

    hex_nums=(textwrap.wrap(nums,4))
    print(hex_nums)    

    return hex_nums




def sum(hex_nums,checksum):
    sum=0
    for i in range(len(hex_nums)):
        sum += int(hex_nums[i], 16)
    sum+=int(checksum,16)
    sum = hex(sum)

    fsum=sum[2:]

    while (len(fsum)>4):
        carry=fsum[0]
        fsum=fsum[1:]
        sum2=hex(int(carry,16)+int(fsum,16))


    tosend=sum2[2:]

    checksumlist=[]
    for i in tosend:
        checksumlist.append(hex(15-int(i,16)))
    for i in range(len(checksumlist)):
        f=checksumlist[i]
        checksumlist[i]=f[2:]

    checksum=''.join(str(x) for x in checksumlist)
    return checksum

print("--Sender--")
inp_str=input("Enter the text ")
initialchecksum="0000"
hex_nums=hexConvert(inp_str)
checksum=sum(hex_nums,initialchecksum)


print("Checksum sent =",checksum)

print("--Receiver--")
inp_str2=input("Enter the text ")
checksum2=input("Enter the checksum ")

hex_nums2=hexConvert(inp_str2)
checksum3=sum(hex_nums2,checksum2)


check=int(checksum3,16)
if(check==0):
    print("Data is unaltered")
else:
    print("Data has been altered")