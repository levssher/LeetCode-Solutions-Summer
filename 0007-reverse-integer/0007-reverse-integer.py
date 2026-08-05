class Solution:
    def reverse(self, x: int) -> int:
        result=0
        sign = 1

        if(x<0):
            sign= (-1)
            x*=(-1)
            

        while(x!=0):
            #make sure the result doesn't overflow 32-bits
            if (result > 214748364) or (result == 214748364 and x%10>7):
                return 0

            result=result*10 + x%10

            x//=10
        
        return result*sign