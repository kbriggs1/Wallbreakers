class Solution:
    def generateParenthesis(self,n):
        output=['']
        nbpass=0
        while nbpass < 2*n:
            oldoutput=output[:]
            output = []
            for par in oldoutput:
                nbclose = par.count(')')
                nbopen = par.count('(')
                if nbopen < n:
                    output.append(par+"(")
                if nbclose < n and nbclose < nbopen:
                    output.append(par+")")
            nbpass+=1
        return output
