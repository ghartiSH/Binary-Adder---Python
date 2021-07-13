def Input():
    try:
        num=int(input())
    except:
        print("Error! Enter a valid Integer(0-9).")
        num=Input()
    toSend = Check(num)
    return toSend

def Check(number):
    if number >= 0 and number < 256:
        return number
    else:
        while number < 0 or number > 256:
            print("Please!..Re-enter the correct number between 0-255")
            number=Input()
        return number
