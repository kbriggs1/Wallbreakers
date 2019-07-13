class Solution(object):
    def fizzBuzz(self, n):
        product = []
        for c in range(1, n+1):
            if c % 15 == 0: 
                product.append("FizzBuzz")
            elif c % 3 == 0: 
                product.append("Fizz")
            elif c % 5 == 0: 
                product.append("Buzz")
            else: product.append(str(c)) 

        return product
        """
        :type n: int
        :rtype: List[str]
        """
        
