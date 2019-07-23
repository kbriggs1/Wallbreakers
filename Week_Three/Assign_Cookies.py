class Solution:
    def findContentChildren(self, childs, cookies):
        """
        :type childs: List[int]
        :type cookies: List[int]
        :rtype: int
        """
        sorted_childs = sorted(childs)
        sorted_cookies = sorted(cookies)
        count = 0
        try:
            for cookie in sorted_cookies:
                if sorted_childs[count] <= cookie:
                    count += 1
        except IndexError:
            print('peak max num of child.')
        finally:
            return count
        
