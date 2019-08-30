# method 1: O(n), Manacher's method, use symmetry of a Palindrome
# utilize the information of previous checked Palindromes
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        if len(s) < 2: return s
        
        s1 = ["#"]
        for c in s:
            s1.append(c)
            s1.append("#")  # add padding to differentiate odd and even palindromes, such as "aa" "aba"
        
        dp = [1]*len(s1)  # dp[i] is the radius of the palindrome centered at s1[i], radius include the center
        
        iLongest = 1  # index of center of longest Palindrome
        
        farest_center = 1  # the center of the farest palindrome visited
        farest_front = 1  # the rightmost index of the farest palindrome visited
        
        for i in range(1, len(s1)):
            if i < farest_front:  # use symmetry of Palindrome
                dp[i] = min(farest_front - i + 1, dp[2*farest_center - i])
            while i + dp[i] < len(s1) and i - dp[i] >= 0 and s1[i+dp[i]] == s1[i-dp[i]]:
                dp[i] += 1
            if i + dp[i] - 1 > farest_front:  # update front
                farest_center = i
                farest_front = i + dp[i] - 1
            if dp[i] > dp[iLongest]:  # update longest palindrome
                iLongest = i
        
        longest_start = (iLongest - dp[iLongest] + 1)//2   # be careful about the index, odd and even palindromes
        longest_len = dp[iLongest] - 1
        return s[longest_start: longest_start + longest_len]

# method 1: brute force, O(n^3), Time limit exceeded (TLE)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = (0,0)
        
        for i in range(len(s)-1):
            for j in range(i, len(s)):
                if (j-i+1) > res[1]-res[0]+1 and self.isPalindrome(s, i, j):
                    res = (i, j)
        return s[res[0]:res[1]+1]
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
