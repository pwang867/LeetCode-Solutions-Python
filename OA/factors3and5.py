# time O(log(n)/log(5))
import math
def helper(num):
	k = 1
	total = 0
	while k <= num:
		total += 1 + int(math.log(num//k)/math.log(3))
		k *= 5
	return total

def getIdealNums(l, r):
	return helper(r) - helper(l)

if __name__ == "__main__":
    print(getIdealNums(200, 405))

