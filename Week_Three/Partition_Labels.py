class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        positions = {k:i for i,k in enumerate(S)}
        res = []
        begin = 0
       
        max_position = 0
    
        for i, k in enumerate(S):
            max_position = max(max_position, positions[k])
           
            if max_position > i: 
                continue
            
            word = S[begin:i+1]
           
            res.append(len(word))
            begin = i+1
        return res
