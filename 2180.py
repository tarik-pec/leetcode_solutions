
#2180. Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

class Solution:
    def countEven(self, num: int) -> int:
        ans = []
        #For each positive integer less than num, check if the integers digits sum to an even number. If so, add it to an array.
        for i in range(1,num+1):
            if self.digitSum(i)%2==0:
                ans.append(i)
        return len(ans)
            
    def digitSum(self, n):
        n = str(n)
        sum = 0
        #Iterate over the digits of the input integer by converting it to a str, then sum them by converting them back. (Not the most elegant solution; I should have used modulus and powers of ten.)
        for digit in n:
            sum = sum + int(digit)
        return sum
        
