#Question: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors):
        if len(colors) < 3:
            return False

        numMovesAlice = 0
        numMovesBen = 0
        consecA = 0
        consecB = 0
        j = len(colors)-1
        for i in range(0, len(colors)):
            if colors[i] == "A":
                consecA+=1
            else:
                numMovesAlice+=max(0, consecA-2)
                consecA = 0
            if colors[j] == "B":
                consecB +=1
            else:
                numMovesBen +=max(0, consecB-2)
                consecB = 0
            j-=1
        #add left overs
        numMovesAlice+=max(0, consecA-2)
        numMovesBen+=max(0, consecB-2)
        return numMovesAlice > numMovesBen
    
                
        
            
if __name__ == "__main__":
    s =  Solution()
    print(s.winnerOfGame("AAAAABBBBBBAAAAA"))
