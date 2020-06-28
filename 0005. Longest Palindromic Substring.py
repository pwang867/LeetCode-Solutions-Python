# method 4: time/sapce O(n), Manacher's method, use symmetry of a Palindrome
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
        
        # be careful about the index, odd and even palindromes
        # palindrome in s1 must start with "#", followed by a letter "x"
        # relation of index i of "#" in new string and index j of the letter "x" in s is j = i//2
        
        # or: get substring from s1 and remove all "#"
        longest_start = (iLongest - dp[iLongest] + 1)//2   
        longest_len = dp[iLongest] - 1
        return s[longest_start: longest_start + longest_len]

# method 3: simplified from method 2, but use a smarter way 
# to deal with odd and even length of palindromes
# time O(n^2), space O(1)
class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        
        for i in range(2*len(s)-1):
            # initialize (left, right) to (0,0),(0,1), (1,0), (1,1),...
            left = i // 2
            right = left + i%2
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left, right = left-1, right+1
            left, right = left+1, right-1
            if right - left > end - start:
                start, end = left, right
        
        return s[start:end+1]

# method 2: Time O(n^2), start search from the center of Palindromes
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0  # the position of the longest palindrome
        
        for i in range(len(s)):
            # search palindromes with odd length
            left, right = self.searchPalindrome(s, i, i)
            if right-left > end-start:
                start, end = left, right
            # search palindromes with even length
            left, right = self.searchPalindrome(s, i, i+1)
            if right-left > end-start:
                start, end = left, right
        
        return s[start:end+1]
    
    def searchPalindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return (i+1, j-1)
        

# method 1: brute force, O(n^3), Time limit exceeded (TLE)
class Solution1(object):
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
    
