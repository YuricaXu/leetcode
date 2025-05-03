class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:#Check for Negative Number
            return False

        reverse = 0#Initialize Variables
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)#reverse the Number
            x //= 10
        
        return reverse == xcopy#Check for Palindrome