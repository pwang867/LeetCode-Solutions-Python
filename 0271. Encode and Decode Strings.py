# method 2: always use 4-byte string to record the length of the str, no delimiter used
# method 2 is better than method 1
class Codec:
    def int_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        print([x >> (i * 8) & 0xff for i in range(4)])
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.int_to_str(len(s)) + s.encode('utf-8') for s in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output


# method 1: use (length + "/" + str) to encode, 
# use more space than method 2 if the length of strs are > 1000
class Codec1:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("/")          # can be any character
            res.append(s)
        return "".join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        num = 0
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
                i += 1
            elif s[i] == "/":
                i += 1
                strs.append(s[i:i+num])
                i += num
                num = 0    # don't forget
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))




test = Codec()
strs = ["abd", "sdfsdfsfafdsafdsf", "egwoiawoiu9489324nmksdjfk"]
encoded_s = test.encode(strs)
print(encoded_s)
decoded_s = test.decode(encoded_s)
print(decoded_s)


"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

 

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
"""
