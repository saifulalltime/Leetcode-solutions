from functools import reduce

def generate(nums1, nums2):
    ans = []
    
    for i in nums1:
        detector = False
        for j in range(nums2.index(i) + 1, len(nums2)):
            if nums2[j] > i:
                ans.append(nums2[j])
                detector = True
                break

        if not detector:
            ans.append(-1)   
    return ans     

# nums1 = [1,3,5,2,4]
# nums2 = [6,5,4,3,2,1,7]                                                     
nums1 = [4,1,2]
nums2 = [1,3,4,2]


callValue = generate(nums1, nums2)
print(callValue)   
