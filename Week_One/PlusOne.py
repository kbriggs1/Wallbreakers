class Solution(object):
    #Unable to solve but will fix before Fri
    def plusOne(self, digits):
        value = str(digits[-1] + 1)
        if "0" not in value:
            digits[-1] = int(value)
        else:
            digits.pop()
            digits += [int(k) for k in list(value)]
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
