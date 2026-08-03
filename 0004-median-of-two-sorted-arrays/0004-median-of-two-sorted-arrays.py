class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)

        #For better readability I always put smaller array on the left
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low=0
        high=m

        while low<=high:
            i=(low+high)//2 #index of median on the num1
            j=(m+n+1)//2-i #index of median on the num2
            
            #find index on the left nums1
            if i==0:
                left_A=-float('inf')
            else:
                left_A=nums1[i-1]
            
            #find index on the right nums1
            if i==m:
                right_A=float('inf')
            else:
                right_A=nums1[i]

            #find index on the left nums2
            if j==0:
                left_B=-float('inf')
            else:
                left_B=nums2[j-1]
            
            #find index on the right nums2
            if j==n:
                right_B=float('inf')
            else:
                right_B=nums2[j]

            #found the perfect cut
            if max(left_A, left_B) <= min(right_A, right_B):
                if (m+n)%2==0:
                    return (max(left_A, left_B)+min(right_A, right_B) )/ 2
                return max(left_A, left_B)
            
            #took too much on the left
            elif left_A > right_B:
                high=i-1
            #took too little on the left
            else:
                low=i+1
