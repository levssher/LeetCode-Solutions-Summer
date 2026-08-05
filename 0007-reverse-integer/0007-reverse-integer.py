class Solution:
    def reverse(self, x: int) -> int:
        result=0

        if(x<0):
            sign= (-1)
            x*=(-1)
        else:
            sign = 1

        while(x!=0 and -2**31 <= result <= 2**31 - 1):

            result*=10
            result+=x%10

            x//=10

        result*=sign
        if result<-2**31 or result>(2**31 - 1):
            return 0
        
        return result