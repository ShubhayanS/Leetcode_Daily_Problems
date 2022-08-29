# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        elif(num%2 ==0 ):
            return 1+ self.numberOfSteps(num//2)
        return 1 + self.numberOfSteps(num-1)
        
        
###### faster solution ######
class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
    
        while num > 0:
            num = (num / 2) if (num % 2 == 0) else (num - 1)
            counter += 1
        
        return counter
