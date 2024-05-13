# Selection sort in Python


def selectionSort(nums):
   
    for step in range(len(nums)):
            min_index = step
            m_str = str(nums[step])
            
            for i in range(step+1,len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i

            temp = nums[step]
            nums[step] = nums[min_index]
            nums[min_index] = temp 


data = [3,30,34,5,9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)