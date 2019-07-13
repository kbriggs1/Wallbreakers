class Solution:
    def isPalindrome(self, word: str) -> bool:

    # def isPalindrome(word):
        letters = []
        lettersReversed = []
        for char in word:
            if char.isalpha() or char.isdigit():
                letters.insert(0, char.lower())
                lettersReversed.append(char.lower())

#         reverse = words.copy()
        # reverse.reverse()

        print(lettersReversed)
        print(letters)
      
        return letters == lettersReversed
        #return words == reverse

story = "A man, a plan, a canal: Panama"
# story1 = "race a car"
raceCar = Solution()
print(raceCar.isPalindrome(story))
    # print(isPalindrome(story1))
