class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        long = None
        maxlen = 0
        look_up = set(words)
        for word in words:
            if len(word) >= maxlen:
                if len(word) == maxlen:
                    if word < long:
                        if all(word[:k] in look_up for k in range(1, len(word))):
                            long = word
                else:
                    if all(word[:k] in look_up for k in range(1, len(word))):
                        long = word
                        maxlen = len(word)
        return long
    
        
