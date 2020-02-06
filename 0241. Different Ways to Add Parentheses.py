# solution2: divide and conquer
# time complexity: O(Catalan_number(n)*n) where n is number of operators

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in self.memo:
            return self.memo[input]
        ans = []
        for i in range(len(input)):
            c = input[i]
            if c in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for x in left:
                    for y in right:
                        if c == "+":
                            ans.append(x+y)
                        elif c == "-":
                            ans.append(x-y)
                        else:
                            ans.append(x*y)
        if not ans:  # edge case: when input is a single number
            ans = [int(input)]
        self.memo[input] = ans
        return ans



# method 2, dynamic programming, time O(Catalan(n)), space: O(n^2*Catalan(n))
# ref: https://www.cnblogs.com/grandyang/p/4682458.html

"""
当然，这道题还可以用动态规划 Dynamic Programming 来做，但明显没有分治法来的简单，
但是既然论坛里这么多陈独秀同学，博主还是要给以足够的尊重的。
这里用一个三维数组 dp，其中 dp[i][j] 表示在第i个数字到第j个数字之间范围内的子串添加
不同括号所能得到的不同值的整型数组，所以是个三位数组，需要注意的是我们需要对 input 字符串进行预处理，
将数字跟操作分开，加到一个字符串数组 ops 中，并统计数字的个数 cnt，用这个 cnt 来初始化 dp 数组的大小，
并同时要把 dp[i][j] 的数组中都加上第i个数字，通过 ops[i*2] 取得，当然还需要转为整型数。
既然 dp 是个三维数组，那么肯定要用3个 for 循环来更新，这里采用的更新顺序跟之前那道 Burst Balloons 
是一样的，都是从小区间往大区间更新，由于小区间之前更新过，所以我们将数字分为两部分 
[i, j] 和 [j, i+len]，然后分别取出各自的数组 dp[i][j] 和 dp[j][i+len]，
把对应的运算符也取出来，现在又变成了两个数组中任取两个数字进行运算，又整两个 for 循环，
所以总共整了5个 for 循环嵌套，啊呀妈呀，看这整的，看不晕你算我输，参见代码如下：
"""

class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        if (input.empty()) return {};
        vector<string> ops;
        int n = input.size();
        for (int i = 0; i < n; ++i) {
            int j = i;
            while (j < n && isdigit(input[j])) ++j;
            ops.push_back(input.substr(i, j - i));
            if (j < n) ops.push_back(input.substr(j, 1));
            i = j;
        }
        int cnt = (ops.size() + 1) / 2;
        vector<vector<vector<int>>> dp(cnt, vector<vector<int>>(cnt, vector<int>()));
        for (int i = 0; i < cnt; ++i) dp[i][i].push_back(stoi(ops[i * 2]));
        for (int len = 0; len < cnt; ++len) {
            for (int i = 0; i < cnt - len; ++i) {
                for (int j = i; j < i + len; ++j) {
                    vector<int> left = dp[i][j], right = dp[j + 1][i + len];
                    string op = ops[j * 2 + 1];
                    for (int num1 : left) {
                        for (int num2 : right) {
                            if (op == "+") dp[i][i + len].push_back(num1 + num2);
                            else if (op == "-") dp[i][i + len].push_back(num1 - num2);
                            else dp[i][i + len].push_back(num1 * num2);
                        }
                    }
                }
            }
        }
        return dp[0][cnt - 1];
    }
};



"""
Given a string of numbers and operators, return all possible results 
from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

input = "2*3-4*5-2*3-4*5-2*3-4*5"
print(len(Solution().diffWaysToCompute(input)))

arr = [0]*15  # arr is the number of different partitions
arr[0] = 1
arr[1] = 1
i = 2
while i < 15:
    for j in range(i):
        arr[i] += arr[j]*arr[i-1-j]
    i += 1
print(arr)
