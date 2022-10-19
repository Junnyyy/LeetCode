class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}
        
        for word in words:
            if word not in wordFreq:
                wordFreq[word] = 1
            else:
                wordFreq.update({word: wordFreq[word] + 1})
        
        response = sorted(wordFreq, key = lambda i: (-wordFreq[i], i))
        
        return response[:k]
            
        
