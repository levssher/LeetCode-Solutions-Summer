class Solution:
    def checkTheString(self, s: str, left:int, right: int):
        len_s=len(s)
        result=""
        while(left>=0 and right<= len_s-1 and s[left]==s[right]):
                if right-left+1>len(result):
                    result=s[left:right+1]
                left-=1
                right+=1
        return result        

    def longestPalindrome(self, s: str) -> str:
        len_s=len(s)
        result=""
        
        
        for i in range(len_s):
            #Palindrome is even 
            even_pol=self.checkTheString(s, i, i+1)
            if(len(result)<len(even_pol)):
                result=even_pol

            #Palindrome is odd
            odd_pol=self.checkTheString(s, i, i)
            if(len(result)<len(odd_pol)):
                result=odd_pol

        return result
                


        

    