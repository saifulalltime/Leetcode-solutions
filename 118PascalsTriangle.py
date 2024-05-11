numRows = 5

arr = [[1]] if numRows == 1 else [[1][1,1]]
    
for i in range(numRows):
    subArr = []
    for j in range(i+1):
        if j == 0 or j == numRows:
            subArr.append(1)
        else:
            subArr.append(arr[i-1])
    arr.append(subArr)  
    # print(arr[0][0])
#     subArr=[]   
print(arr)         