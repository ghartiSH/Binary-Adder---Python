def Convert(dec):
    bit=[]
    binary=[]
    digits=0
    while digits!=8:
        rem = dec%2
        bit.append(rem)
        dec=dec//2
        digits+=1
    binary=ReverseBinary(bit)
    return binary

def ReverseBinary(binaryList):
    actualBinary=[]
    for i in range(len(binaryList)-1,-1,-1):
        actualBinary.append(binaryList[i])
    return actualBinary
