import numpy as np
import math

def ChooseConvert():
    print("""
    [1] Binary -> Decimal
    [2] Decimal -> Binary 
    ----------------------------
    [3] Binary -> Octal 
    [4] Octal -> Binary 
    ----------------------------
    [5] Binary -> Hexadecimal 
    [6] Hexadecimal -> Binary
    [7] Hexadecimal -> Decimal  
    ----------------------------
    [8] Decimal -> Octal 
    [9] Octal -> Decimal 
    [10] Decimal to Hexadecimal 
    ----------------------------
    """)
def GetPerDigit(number):
    converter = [int(x) for x in str(number)]
    return np.array(converter)

def BinaryToDecimal(binary):
    DigitArray = GetPerDigit(binary) # Converts binary to an array
    print("Binary:")
    for y in DigitArray:
        print(y)
    print("--------------------------------------------------")
    power = 0
    decimalValue = 0
    for x in DigitArray: 
        decimalValue += x * math.pow(2,power)
        print(f'{x} x 2^{power} = {x * math.pow(2,power)}')
        power+=1
        print("--------------------------------------------") 

    return f"Decimal Form: {decimalValue}"

# Main 
print("Please input a number:  ")
print(BinaryToDecimal(input()))


