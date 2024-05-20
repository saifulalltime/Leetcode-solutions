from functools import reduce

def generate(nums1, nums2):
    nums1.sort()
    nums2.sort()
    ans = []
    for i in range(len(nums1)):
        for j in range(1,len(nums2)):
            if nums1[i] == nums2[j]:
                
                if nums2[j] > nums2[j-1]:
                    ans.append(nums2[j])
                elif nums2[j] < reduce(max, nums2):
                    ans.append(reduce(max, nums2))
                else:
                    ans.append(-1)   
            elif j == len(nums2)-1 and nums1[i] == nums2[len(nums2)-1]:
                ans.append(-1)
                        
    return ans        

# nums1 = [1,3,5,2,4]
# nums2 = [6,5,4,3,2,1,7]
nums1 = [4,1,2]
nums2 = [1,3,4,2]


callValue = generate(nums1, nums2)
print(callValue)   

#   ans = []
    
#         for i in range(len(nums1)):
#             for j in range(1,len(nums2)):
#                 # print("j",j,"=",nums2[j-1],"==",nums2[j])
#                 # print(nums1[i] ,"==", nums2[j-1])
                
#                 if nums1[i] == nums2[j-1]:
#                     if nums2[j] > nums2[j-1]:
#                         ans.append(nums2[j])
#                     else:
#                         ans.append(-1)   
#                 elif j == len(nums2)-1 and nums1[i] == nums2[len(nums2)-1]:
#                     ans.append(-1)   
#         return ans 