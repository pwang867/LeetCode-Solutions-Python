# amazon OA

class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = filter(lambda x: x[-1] >= "a" and x[-1] <= "z", logs)
        digit_logs = filter(lambda x: x[-1] >= "0" and x[-1] <= "9", logs)
        letter_logs = sorted(letter_logs, 
                    key = lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        letter_logs.extend(digit_logs)
        return letter_logs


if __name__ == "__main__":
    x = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(Solution().reorderLogFiles(x))

