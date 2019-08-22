# method 2: O(1)
# (a^1%1337, a^2%1337, a^3%1337, ...) must have a period <= 1337 
# (x*y%N) = (x%N)*(y%N)
class Solution(object):
    def superPow(self, a, b):
        N = 1337
        a = a%N
        
        d = {} # {x:y} where y = (a**x)%N
        num = 1
        period = 0
        for i in range(1, N+1):
            num = (num*a)%N
            if num in d:
                period = i - d[num]
                break
            d[num] = i
        
        # get simplied b to b <= 1337
        temp = 0  # temp < period
        for x in b:
            temp = (temp*10 + x)%period
        b = temp
        
        res = 1
        for i in range(b):
            res = res*a%N
        return res
    

# method 1: recursion, log(N)
class Solution1(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        N = 1337
        res = 1
        for y in b:
            res = (self.special_exp(res, 10)*self.special_exp(a, y))%N
        return res
    
    
    def special_exp(self, x, y, N=1337):
        # 0 <= y <= 10
        if y == 0:
            return 1
        if y == 1:
            return x%N
        
        if y%2 == 0:
            return (self.special_exp(x, y//2))**2 % N
        else:
            return self.special_exp(x, y//2)**2*x % N
            
