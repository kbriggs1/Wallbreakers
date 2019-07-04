class Solution:
     def countOfAtoms(self, formula):
        counter = collections.Counter()
        N = len(formula)
        
        count = 1 # Integer 
        stack = [] # All counts kept track of
        weight = 1 # common weight = product of all counts in current stack
        
        k = N-1
        
        while k >= 0:
            low = '' #no lower case
            count = 1 # no count specified means count=1
            
            if formula[k].isdigit(): #  calculate count first to use in code
                j = k
                while k>=0 and formula[k].isdigit(): k-=1 # could test if i>=0 after this point, however the problem guarantees an upper case letter on the left
                count = int(formula[k+1:j+1])
            
            
            if formula[k] == ')':
                weight *= count
                stack.append(count)
            
            elif formula[k] == '(':
                weight //= stack.pop()
            
            elif formula[k].islower():
                low = formula[k]
                k-=1 # not testing if i>=0 because the problem guarantees an upper case letter
            
            if formula[k].isupper(): # use upper case in the end which gives all the info
                a = formula[k]+low
                counter[a]+=count*weight
            k-=1
        ans = []
        for a in sorted(counter.keys()):
            ans.append(a)
            if counter[a]>1: ans.append(str(counter[a]))
        return ''.join(ans)



