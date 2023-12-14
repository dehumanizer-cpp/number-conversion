selectedOption = "Null"
def decimalToBinary(decimalValue,digit=8):
    print("*--- DECIMAL TO BINARY")

    listOfZeroAndOne=[]
    for i in range(digit+1):
        if (decimalValue % 2 ==0 ):
            listOfZeroAndOne.append(0)
        else:
            listOfZeroAndOne.append(1)
        decimalValue //= 2
    return ''.join(str(e) for e in listOfZeroAndOne[::-1])#Reversing list and converting list to string

def binaryToDecimal(binaryValue):
    print("*--- BINARY TO DECIMAL")

    binaryValue = str(binaryValue)
    binaryToDecimalValue = 0
    indexOfText = 0
    for letterOnBinaryValue in binaryValue[::-1]:
        if letterOnBinaryValue == "1":
            binaryToDecimalValue += pow(2,indexOfText)
            indexOfText += 1
        else:
            indexOfText += 1

    return binaryToDecimalValue

while selectedOption != "99":
    selectedOption = input(
"""
1) Binary to decimal
2) Decimal to binary
>>>"""
    )

    if selectedOption == "1":
        firstOptionInput = input("Binary value>>> ")
        print(f"{firstOptionInput}'s decimal format is {binaryToDecimal(firstOptionInput)}")
    elif selectedOption == "2":
        secondOptionInput = int(input("Decimal value>>> "))
        secondOptionInputDigit = int(input("-optional- Digit>>> "))
        print(f"{secondOptionInput}'s binary format is {decimalToBinary(secondOptionInput,digit=secondOptionInputDigit)}")
    elif selectedOption == "99":
        print("Program will be closed.")
        break
    else:
        print("You chose wrong option, try again.")


