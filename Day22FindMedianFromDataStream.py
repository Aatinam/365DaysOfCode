#Day 22 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/find-median-from-data-stream/

#Problem Statement : The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

import heapq;
class MedianFinder:
    class Num:
        def __init__(self, value):
            self.val = value;
            
        def __eq__(self, other):
            return self.val == other.val;
        
        def __lt__(self, other):
            return not(self.val < other.val)
                

    def __init__(self):
        """
        initialize your data structure here.
        """
        #heap of half the size of list. 
        #that contains the lower half or upper half 
        #if it contains upper half heap.pop will return lowest element in           #the upper half which is median, and if element we are now adding
        #is bigger than the smallest element in the list 
        self.Right = []
        self.Left = []
        self.size = 0

    def addNum(self, num):
        self.size+=1;
        heapq.heappush(self.Left, self.Num(num));
        reqHeapSize = (self.size)//2;
        if len(self.Right) < reqHeapSize:
            largestNumFromLeft = heapq.heappop(self.Left);
            heapq.heappush(self.Right, largestNumFromLeft.val );
        elif len(self.Right) > 0 and self.Right[0] < num:
            smallestNumFromRight = heapq.heappop(self.Right);
            heapq.heappop(self.Left); #Largest num from Left must be num. This is because Right heap is made up of largest values from the left heap. So if there is an         
                                      #element that is larger than the smallest elelemnt on the right, it must be larger than 
            heapq.heappush(self.Right, num);
            heapq.heappush(self.Left, self.Num(smallestNumFromRight));

    def findMedian(self):
        if self.size % 2 != 0:
            return self.Left[0].val
        return (self.Left[0].val + self.Right[0])/2


if __name__ == "__main__":
    m = MedianFinder();
    m.addNum(1)
    m.addNum(2)
    print(m.findMedian())
    m.addNum(3)
    print(m.findMedian());
    #size = 1, Left=[1], size = 2, left = [1] Right = [2].  size =3, left = [2,1] R=[3]  
