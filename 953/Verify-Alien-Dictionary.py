class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {}

        for i in range(len(order)):
            map[order[i]] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
        
            shortestLength = min(len(word1), len(word2))
            flag = False

            for j in range(shortestLength):
                if map[word1[j]] < map[word2[j]]:
                    flag = True
                    break
                elif map[word1[j]] > map[word2[j]]:
                    return False
            
            if not flag and len(word1) > len(word2):
                return False
        
        return True
