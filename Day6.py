
#Day 6 of 365 days of code
#I solved the following question from leetcode: 

#Problem Statement 


class Solution:
    def climbStairs(n):
        ans = [];
        def stairHelper(stairsLeft , stepsTaken):
            if stairsLeft == 0:
                b = stepsTaken[:];
                ans.append(b);
                print(stepsTaken);
                
            for stepVal in [1, 2]:
                if stepVal <= stairsLeft:
                    stepsTaken.append(stepVal);
                    stairHelper(stairsLeft - stepVal, stepsTaken);
                    #backTrack
                    stepsTaken.pop();
                
        stairHelper(n, []);
        print(ans);
        return len(ans);       


    if __name__ == "__main__":

            climbStairs(4);
       
