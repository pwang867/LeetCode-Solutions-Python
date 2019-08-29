# this question is basicly asking for the count of divisors of a number
# only lighbulbs in m^2 will be on, becuase dividors will always 
# appears in a pair except m^2, so only m^2 will have odd numbers of dividors

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(pow(n, 0.5))
    
