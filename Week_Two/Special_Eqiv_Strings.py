class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = []
        for string in A:
            even = [string[char] for char in range(0, len(string), 2)]
            odd  = [string[char] for char in range(1, len(string), 2)]
            even = sorted(even)
            odd  = sorted(odd)
            output = even + odd
            if output in groups:
                continue
            groups.append(output)

        return len(groups)
