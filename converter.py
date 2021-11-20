import numpy as np
import math
import array

from numpy.lib.function_base import append, digitize



def GetPerDigit(number):
    converter = [int(x) for x in str(number)]
    return np.array(converter)
def BinaryToDecimal(binary): # Finished bug free
    DigitArray = GetPerDigit(binary) # Converts binary to an array
    reversedDigitArray = DigitArray[::-1] # Invert the array
    print("Binary:")
    for y in reversedDigitArray:
        print(y)
    print("--------------------------------------------------")
    power = 0
    decimalValue = 0
    for x in reversedDigitArray: 
        decimalValue += x * math.pow(2,power)
        print(f'{x} x 2^{power} = {x * math.pow(2,power)}')
        power+=1
        print("--------------------------------------------") 

    return print(f"Decimal Form: {int(decimalValue)}")
def DecimalToBinary(decimal): # Finished bug free
    binaryArray = [] 
    binaryArrayCleaned = []
    try:
        while 2/int(decimal) != 0: # Modulo the number to find if there is a remainder
            print(f'2 / {decimal} = {int(decimal)%2}')
            binaryArray.append(binaryArray.append(int(decimal)%2)) # Adds the value the list 
            decimal/=2
    except:
        if decimal > 2:
            pass
    for num in binaryArray: # Removes the None values in the list 
        if num != None: 
            binaryArrayCleaned.append(num)
    return print(binaryArrayCleaned[::-1]) # Returns it in reverse


def ViewMenu():
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
    """)

def ChooseConvert(num,choice):
    if choice == "1":
        BinaryToDecimal(num)
    elif choice == "2":
        DecimalToBinary(num)
    else:
        print("hello world")

    

# Main 
ViewMenu()
print("Please input a number:")
ChooseConvert(int(input()),input()) 


