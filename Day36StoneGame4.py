class Solution:
    
    def stoneGameIX(self, stones):
        
        freqCache = [0]*3
        for i in range(0, len(stones)):
            rem = stones[i] % 3
            freqCache[rem]+=1

        #if Bob picks a zero and Alice picks a zero, the zeroes
        #cancel out. So we can reduce the number of zeroes
        #in our freqCache by 2. 
        freqCache[0] = freqCache[0] % 2
        
        #Alice can't start from zero, she will lose, so she starts from
        #either 2 or one. If she can find a winning route by starting with
        #either 2 or 1 she wins, else Bob wins
        n = sum(freqCache) #Not len(stones) since we have to adjust length since we removed some zeroes. 
        return self.stoneGame(freqCache, 1,n ) or self.stoneGame(freqCache, 2, n)
    
    
    def stoneGame(self, freqCache, start, n):
        if (not freqCache[start]):
            return False
        
        temp = freqCache[:]
        stoneSum = start
        temp[start]-=1
        AliceTurn = False
        for i in range(1, n): #starting with 1 because first turn taken
            noStonePicked = True
            for i in range(0, 3):
                if (not temp[i]) or ((i+stoneSum) % 3) == 0:
                    continue
                stoneSum+=i
                temp[i]-=1
                noStonePicked = False
                break;
                
            if noStonePicked:
                if AliceTurn:
                    return False
                return True
            AliceTurn = not AliceTurn
            
        return False     
            
                

                
if __name__ == "__main__":
    sol = Solution()
    sol.stoneGameIX([3,3,1])
                        
            
                    
            

        