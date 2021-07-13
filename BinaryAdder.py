def Adder(bitList1,bitList2):
    toLoop = len(bitList1)
    sumList=[]
    carry = 0
    for i in range(toLoop-1,-1,-1):
        bitA=bitList1[i]
        bitB=bitList2[i]
        summ=bitA^bitB^carry
        sumList.append(summ)
        carry=(carry&(bitA^bitB))|(bitA&bitB)
    sumTotal= ReverseSum(sumList)
    return sumTotal

def ReverseSum(sumList):
    actualSum=""
    newList=[]
    for i in range(len(sumList)-1,-1,-1):
        if sumList[i]==1:
            for j in range(i,-1,-1):
                newList.append(sumList[j])
            break
    for k in range(0,len(newList)):
        actualSum=actualSum + str(newList[k])    
    return actualSum
