class Solution(object):
    def reverse(self, x):
        reversed_x = 0
        original_x = x  
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
       
        if original_x < 0:
            reversed_x = -reversed_x
        
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x
    