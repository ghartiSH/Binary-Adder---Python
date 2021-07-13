import BinaryAdder
import BinaryToDecimal
import InputValidation
def Functional():
    print("Enter the first number")
    num1=InputValidation.Input()
    print("Enter the second number")
    num2=InputValidation.Input()
    bin1=BinaryToDecimal.Convert(num1)
    bin2=BinaryToDecimal.Convert(num2)
    toPrint = BinaryAdder.Adder(bin1,bin2)
    if toPrint=="":
        print("The binary addition of integers",num1,"and",num2,"is",0)
    else:
        print("The binary addition of integers",num1,"and",num2,"is",toPrint)
