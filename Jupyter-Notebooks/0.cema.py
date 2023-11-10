import numpy as np

"""
# convert a binary string to an integer
intValue = int('0b00000011', 2)
print(intValue) #prints the ingeter value

# convert integer value to binary
binaryValue = format(intValue, '08b')
"""

def getHammingWeight(integer):
    '''
    This function takes an integer and returns the hamming weight.
    '''
    string = format(integer, '08b')    
    count = 0
    for i in range(len(string)):
        if(int(string[i]) == 1):
            count = count + 1
    return count


def genPlainTexts(plainTextLength, numPlainTexts):
    '''
    This function generates a matrix of plaintexts and return as a numpy array.
    plainTextLength = length of the plaintext in bits
    numPlainTexts = number of plaintexts to generate
    '''
    plainTexts = np.random.randint(256, size=(numPlainTexts, plainTextLength))
    return plainTexts


def genHypoMatrix(plainTexts, keyByteIndex):
    '''
    This function generates the hypothesis matrix for the first byte of the key
    by taking a numpy array which has the first bytes of all the plain texts.
    
    plainTextBytes = plain text numpy array
    keyByteIndex = the index of key byte hypothesized by this hypothetical matrix
    '''
    plainTextBytes = plainTexts[:,keyByteIndex:keyByteIndex+1]

    # hypotheis matrix is 256xN long (N is the number of plain texts)
    H = np.zeros(shape=(256, len(plainTextBytes)), dtype=int)
    #print(H)
    
    for i in range(len(plainTextBytes)):
        #print(format(plainTextBytes[i][0], '08b'))
        plainByte = plainTextBytes[i][0]
        for j in range(256):       
            #print(format(j, '08b'))
            keyByte = j
            # XOR operation between the plain text byte and key byte
            result = plainByte ^ keyByte
            #print(format(result, '08b'))
            #print(getHammingWeight(result))
            H[j,i] = getHammingWeight(result)
    return H

def getHypoMatrices(plainTexts, keyLengthInBytes):
    '''
    This function generates the hypothesis matrix of each key byte and return them
    as a tuple. Each element of the tuple is a hypothetical matrix.
    
    plainTextBytes = plain text numpy array
    keyLengthInBytes = number of bytes in the key
    '''
    H_all = ()
    
    for i in range(keyLengthInBytes):
        H = genHypoMatrix(plainTexts, i)
        #print(H)
        H_all = H_all + (H,)

    return H_all


def genEMTraces(realKey, plainTexts, traceDuration, noiseLevel):
    '''
    This function takes the real key, plaintext matrix and trace duration as input
    in order to generate EM trace matrix for testing purposes.
    '''
    # trace matrix size is (traceDuration X number_of_plain_texts)
    #T = np.zeros(shape=(traceDuration, len(plainTexts)), dtype=int)
    #T = np.ones(shape=(traceDuration, len(plainTexts)), dtype=int)
    #T = np.random.randint(2, size=(traceDuration, len(plainTexts)))
    #T = np.random.randint(10, size=(traceDuration, len(plainTexts)))
    
    T = np.random.randint(noiseLevel, size=(traceDuration, len(plainTexts)))

    for i in range(len(plainTexts)):
        for j in range(len(realKey)):
            result = plainTexts[i][j] ^ realKey[j]
            hw = getHammingWeight(result)
            #T[j,i] = hw
            T[j,i] = T[j,i] + hw
            
    return T


def getCorrelationCoefficient(variable1, variable2):
    '''
    This function returns the correlation coefficient of two python lists
    '''
    correlation = np.corrcoef(variable1, variable2)[1,0]
    return correlation


def buildCorrelationMatrix(hypoMatrix, traceMatrix):
    '''
    This function takes hypothetical matrix and tracematrix to produce correlation
    matrix.
    '''
    # creating correlation matrix (for the first key byte for time being)
    C = np.zeros(shape=(len(hypoMatrix), len(traceMatrix)), dtype=float)
    #print(C.shape)
    
    for i in range(len(hypoMatrix)):
        for j in range(len(traceMatrix)):
            cor = getCorrelationCoefficient(hypoMatrix[i].tolist(), traceMatrix[j].tolist())
            C[i, j] = cor
    
    #print(np.unravel_index(C.argmax(), C.shape))
    return C


def recoverKey(hypoMatrixAll, traceMatrix, keyLengthInBytes):
    '''
    This function takes all the hypothesis matrices and EM trace matrices, build
    corelation matrices for each key byte in order to recover the key.
    hypoMatrixAll = a tuple variable where each tuple element is a hypothetical matrix
    traceMatrix = EM trace matrix
    keyLengthInBytes = number of bytes in the actual key
    '''
    key = np.empty([0,0])
    
    for i in range(keyLengthInBytes):
        C = buildCorrelationMatrix(hypoMatrixAll[i], traceMatrix)
        (keyByte, timeIndex) = np.unravel_index(C.argmax(), C.shape)
        key = np.append(key, keyByte)
        
    #return key
    return key.astype(int)

###############################################################################
#           Depreciated functions                                             #
###############################################################################

"""
def getHexChar(bitsList):
    '''
    This function takes a list containing 4 bits and return the corresponding
    hex charactor.
    bitsList = [0, 1, 0, 1]
    '''
    
    # converting the list to a string
    bitString = ""
    for i in bitsList:
        bitString = bitString + str(i)
    
    # finding the corresponding hex value for the string
    if(bitString == "0000"):
        hexString = "0"
    elif(bitString == "0001"):
        hexString = "1"
    elif(bitString == "0010"):
        hexString = "2"
    elif(bitString == "0011"):
        hexString = "3"
    elif(bitString == "0100"):
        hexString = "4"
    elif(bitString == "0101"):
        hexString = "5"
    elif(bitString == "0110"):
        hexString = "6"
    elif(bitString == "0111"):
        hexString = "7"
    elif(bitString == "1000"):
        hexString = "8"
    elif(bitString == "1001"):
        hexString = "9"
    elif(bitString == "1010"):
        hexString = "A"
    elif(bitString == "1011"):
        hexString = "B"
    elif(bitString == "1100"):
        hexString = "C"
    elif(bitString == "1101"):
        hexString = "D"
    elif(bitString == "1110"):
        hexString = "E"
    elif(bitString == "1111"):
        hexString = "F"
    else:
        print("Wrong string")     
    return hexString

def getHexFromBitList(bitsList):
    '''
    This function takes list of bits of any length and return the corresponding
    hex value string.
    '''
    
    # convert the list to a numpy array
    bits = np.array(bitsList)
    
    # reshaping the 1D array to a Nx8 matrix
    numBytes = int(len(bits)/8)
    bits = bits.reshape((numBytes, 8))
    
    # the variable to contain final hex string
    hexString = ""
    
    # processing each byte
    for i in range(numBytes):
        
        # breaking byte to two segments each with 4 bits
        byte = bits[i].reshape((2,4))
        
        # processing first 4 bits
        hexString = hexString + getHexChar(byte[0].tolist())
        # processing second 4 bits
        hexString = hexString + getHexChar(byte[1].tolist())
        # adding a space to separate bytes
        hexString = hexString + " "
        
    return hexString
"""