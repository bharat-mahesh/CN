import textwrap

def hexConvert(inp_str):
    inp_arr=[x for x in inp_str]

    hex_arr=[]
    for i in inp_arr:
        hex_char=(hex(ord(i)))
        hex_arr.append(hex_char[2:])


    nums=''.join(hex_arr)
    hex_nums=(textwrap.wrap(nums,4))
    return hex_nums


def sum(hex_nums,checksum):
    sum=0
    for i in range(len(hex_nums)):
        sum += int(hex_nums[i], 16)
    sum+=int(checksum,16)
    sum = hex(sum)


    fsum=sum[2:]

    if (len(fsum)>4):
        carry=fsum[0]
        newsum=fsum[1:]


    sum2=hex(int(carry,16)+int(newsum,16))

    tosend=sum2[2:]


    checksumlist=[]
    for i in tosend:
        checksumlist.append(15-int(i,16))
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
hex_nums2=hexConvert(inp_str2)
checksum2=sum(hex_nums2,checksum)

print("Checksum at receiver =",checksum2)

check=checksum2.find('1')
if(check==-1):
    print("Data is unaltered")
else:
    print("Data has been altered")