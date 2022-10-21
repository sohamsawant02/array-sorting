class Solution:
    def singleNonDuplicate(self,nums):
        low=0
        high=len(nums)-1
        mid=0
        if(high==0):
            print(nums[0])
        elif(nums[0]!=nums[1]):
            print(nums[0])
        elif(nums[high]!=nums[high-1]):
            print(nums[high])

        while(low<=high):
            mid=low+(high-low)//2
            if(nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            #if that maintain both conditions 
            if(((mid%2)==0 and nums[mid]==nums[mid+1]) or ((mid%2)==1 and nums[mid]==nums[mid-1]))):
                low=mid+1
            else:
                high=mid-1
        print(-1)
            
                

t=Solution()
num=[2,1,1]
t.singleNonDuplicate(num)
