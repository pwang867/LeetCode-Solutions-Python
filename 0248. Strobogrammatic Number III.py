# time O(len(high)), space O(1)
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        ans = 0
        high = str(int(high)+1)
        n1 = len(low)
        n2 = len(high)
        if n1 > n2:
            return 0
        
        for n in range(n1 + 1, n2 + 1):
            ans += 4*self.core(n - 2)
        
        ans += self.above(n1, low)
        ans -= self.above(n2, high)
        
        return ans
    
    def core(self, n):
        # get counts of length n cores of strobogrammatic numbers
        # core means stripped strobogrammatic number
        # core can start with "0"
        # core(0) = 1
        if n%2 == 0:
            return 5**(n/2)
        if n%2 == 1:
            return 3*5**((n - 1)/2)
    
    def above(self, n, num):
        # return the count of strobogrammatic numbers with length n and larger or equal than num
        if n != len(num):
            raise ValueError("Condition n == len(num) must be satisfied.") 
        ans = 0
        _set = set(['0', '1', '6', '8', '9'])
        d = {'0':4, '1':3, '2':3, '3':3, '4':3, '5':3, '6':2, '7':2, '8':1, '9':0}
        for i in range(n/2):  # scan digits one by one
            ans += d[num[i]]*self.core(n - 2*i - 2)  # add cnts for each digits
            if num[i] not in _set:
                break
        else:
            ans += self.center(num)
        return ans
    
    
    def center(self, num):
        """ 
        to check how many strobos are larger or equal to num 
        if the first n/2 letters are the same
        """
        n = len(num)
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}  # 2:2 not strobogrammatic, do not forget 0:0
        ans = 0
        if n%2 == 0:
            for i in range(n/2):
                if pairs[num[i]] < num[-i - 1]:  
                    # not necessary to change to int, int(num[i]) > int(strobo[i])
                    return 0
            return 1
        else:
            c = num[n/2]  # center character
            _set = {'0', '1', '8'}
            if c == '0':
                ans += 2
            elif "1" <= c <= "7":
                ans += 1
            if c not in _set:
                return ans
            else:
                for i in range(n/2):
                    if pairs[num[i]] < num[-i - 1]:
                        return ans
                return ans + 1
    



class Solution1:
    # @param {string} low
    # @param {string} high
    # @return {integer}
    def strobogrammaticInRange(self, low, high):
        a=self.below(high)
        b=self.below(low,include=False)
        return a-b if a>b else 0
    
    '''
    get how many strobogrammatic numbers less than n
    '''
    def below(self, n, include=True):
        res = 0
        for i in range(1, len(n)):
            res += self.number(i)
        nums = self.strobogrammatic(len(n))
        '''
        filter num larger than n and start with 0
        '''
        if include:
            filtered = [num for num in nums if (len(num)==1 or num[0]!='0') and num <= n]
        else:
            filtered = [num for num in nums if (len(num)==1 or num[0]!='0') and num < n]
        return res + len(filtered)
    
    '''
    get all strobogrammatic numbers with length n,
    number starting with 0 would be included
    '''
    def strobogrammatic(self, n):
        res=[]
        if n == 1:
            return ['0','1','8']
        if n == 2:
            return ['00','11','69','96','88']
        for s in self.strobogrammatic(n-2):
            res.append('0'+s+'0')
            res.append('1'+s+'1')
            res.append('6'+s+'9')
            res.append('8'+s+'8')
            res.append('9'+s+'6')
        return res
    
    '''
    get total counts of strobogrammatic numbers of length n
    '''
    def number(self,n):
        if n == 0:
            return 0
        if n%2 == 0:
            return 4*(5**(n/2-1))
        if n == 1:
            return 3
        return 3*(5**(n/2-1))*4


"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers 
that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""
