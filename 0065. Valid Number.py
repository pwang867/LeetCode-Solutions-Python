# 0. strip space
# 1. only "+/-", digit, "." and "eE" can appear, other characters are not allowed
# 2. "+-" can only appear in the beginning, and can be processed first
# 3. we can only have one "+/-" before and after "e", "E"
# 4. "." can only appear at most once only before "e" or "E"
# 5. "." must have a number either before or after it
# 6. we must have at least one digit before and after "e", e-9 is false, 9.2e is false


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:  # empty string
            return False
        
        start = 0
        if s[0] in "+-":  # the beginning of the string s can be "+" or "-"
            start = 1
        
        has_dot = False
        has_digit = False
        for i in range(start, len(s)):
            letter = s[i]
            if letter.isdigit():
                has_digit = True
                continue
            elif letter == ".":  # "2.e-9 True", ".2e-9 True", ".e-9 False"
                if has_dot:
                    return False
                has_dot = True
                if (i==0 or not s[i-1].isdigit()) and (i==len(s)-1 or not s[i+1].isdigit()):
                    return False  # "." must have a number either before or after it
            elif letter == "e" or letter == "E":
                if not has_digit:  # e-9 false, we must have a digit before "e"
                    return False
                return self.isInteger(s[i + 1:])
            else: # a2
                return False
        return True
    
    def isInteger(self, num):
        # num: string, can has at most one "+" or "-"
        if not num:
            return False
        if num[0] in ["+", "-"]:
            num = num[1:]
        if not num:
            return False
        return num.isdigit()


"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
"""
