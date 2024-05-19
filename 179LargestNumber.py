
def selectionSort(nums):
    for step in range(len(nums)):
        min_index = step
        m_str = str(nums[step])
        for i in range(step+1,len(nums)):
            firstS = m_str + str(nums[i])
            secondS = str(nums[i]) + m_str
            if firstS < secondS:
                min_index = i
                m_str = str(nums[min_index])

        temp = nums[step]
        nums[step] = nums[min_index]
        nums[min_index] = temp   
    if  nums[0]==0:
        return "0"
    return "".join([ str(x) for x in nums])
             
data = [3,30,34,5,9]

newd = selectionSort(data)
# print('Sorted Array in Ascending Order:')
print(newd)