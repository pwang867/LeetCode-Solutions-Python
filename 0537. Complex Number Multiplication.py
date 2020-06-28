class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_real, a_virtual = self.parseComplexNumber(a)
        b_real, b_virtual = self.parseComplexNumber(b)
        ans_real = a_real * b_real - a_virtual * b_virtual
        ans_virtual = a_real * b_virtual + a_virtual * b_real
        return str(ans_real) + "+" + str(ans_virtual) + "i"

    def parseComplexNumber(self, num):
        # return [real part of num, virtual part of num]
        a, b = num.split("+", 1)
        return [int(a), int(b[:-1])]


if __name__ == "__main__":
    a, b = "1+-1i", "1+-1i"
    res = Solution().complexNumberMultiply(a, b)
    print(res)
