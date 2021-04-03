#Day 18 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/top-k-frequent-words/

#Problem Statement : Given a non-empty list of words, return the k most frequent elements.
#Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

import heapq;

class Solution(object):
    
    class Element:
        def __init__(self, word, count):
            self.word = word;
            self.count = count;
            
        def __eq__(self, other):
            return self.word == other.word and self.count == other.count;
        
        def __gt__(self, other):
            return self.count > other.count or (self.count == other.count 
            and self.word < other.word);
            
    def topKFrequent(self, words, k):
        wordCount = {}
        for word in words:
            if word not in wordCount:
                wordCount[word] = 0
            wordCount[word]+=1
            
        heap = []
        for word in wordCount:
            heapq.heappush(heap, [self.Element(word, wordCount[word]), word ]);  ## Why do we need to put element first ? From Python documentation: When you put the objects (i.e. tuples) into heap, it will take the first attribute in the object to compare. 
                                                                                 ## If a tie happens, the heap will use the next attribute (i.e. value_1) and so on.
                                                                                
            if len(heap) > k: ##Recall that heappop, heappush cost O(logn), where n is the size of the heap. By keeping
                              ##The heap size at at most k, the worst case run time of heappop/push would be log(k)
                heapq.heappop(heap);  
        
        topK = []
        for _ in range(k):
            topK.append(heapq.heappop(heap)[1])
        topK.reverse() ##heap.pop return the smallest element, so we need to reverse it 
        return topK