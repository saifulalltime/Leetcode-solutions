import math

def generate(numRows):

    # Initialize the number of items to choose from
    # n = 4

    # # Initialize the number of possibilities to choose
    # k = 3

    # # Print total number of possible combinations
    # print (math.comb(n, k))

    arr = [] 
    for i in range(numRows):
        newArr = []
        for j in range(i):
            newValue = math.comb(i, j)
            newArr.append(newValue)
        newArr.append(1)
        arr.append(newArr)
    return arr        

callValue = generate(5)
print(callValue)    