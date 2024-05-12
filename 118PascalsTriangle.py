
def generate(numRows):
    arr = [] 
    arr.append([1])
    for i in range(numRows-1):
        newArr = [1]
        for j in range(i):
            newArr.append(arr[i][j]+arr[i][j+1])
        newArr.append(1)
        arr.append(newArr)
    return arr        

callValue = generate(5)
print(callValue)    