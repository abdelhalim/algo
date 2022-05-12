# Leetcode 70
# Climbing Stairs

class Solution:
    dict = dict()

    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        #prev_one_step = self.climbStairs(n - 1)
        #prev_two_steps = self.climbStairs(n - 2)
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        #return prev_two_steps + prev_one_step
        return self.dict[n]

    def climbStairs2(self, n):
        a, b = 1, 1+n%2
        #print ("a = ", a, " b = ", b)
        for i in range(int(n/2)):
            a += b
            b += a
            print (i, " a = ", a, " b = ", b)
        return a

    def climbStairs3(self, n):
        if n <= 2: 
            return n
    
        ways = [0 for _ in range(n)]
        ways[0] = 1
        ways[1] = 2
    
        for i in range(2, n):
            ways[i] += ways[i - 1] + ways[i - 2]
    
        return ways[-1]

def __init__(self):
    self.dict = {1:1, 2:2}


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(39))

    print(sol.climbStairs2(39))

    print(sol.climbStairs3(39))
