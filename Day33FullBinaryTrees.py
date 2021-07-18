
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in xrange(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x): #What's brilliant about this solution is that if null gets returned for left tree or right tree, 
                                                    #then we won't create a tree, for loop will terminate because none was returned. So the only time we create trees is when 
                                                    #there si a child for both left and right. 
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
            

if __name__ == "__main__":
   s = Solution()
   s.allPossibleFBT(7)
                


                