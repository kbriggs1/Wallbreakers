class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==0:
            return len(word2)
        elif len(word2)==0:
            return len(word1)
        else:
            
            W1 = len(word1)+1
            W2 = len(word2)+1
            T=[0]*W2 #row
            for k in range(W2):
                T[k]=[0]*W1 #column
                
            for k in range(W1):
                T[0][k]=k
            for k in range(W2):
                T[k][0] = k
            #now memorizing the previous operation and move forward
            
            for k in range(1,W2):
                for j in range(1,W1):
                    if (word1[j-1]==word2[k-1]):
                        T[k][j] = T[k-1][j-1]
                    else:
                        tmp =min(T[k-1][j],T[k-1][j-1],T[k][j-1])
                        T[k][j] = tmp + 1
                        
            
            return T[W2-1][W1-1]

        
