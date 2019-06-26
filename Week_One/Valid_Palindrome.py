class Solution(object):
    #unable to solve but will work on correcting error by Fri
    def fn(s):
        words = []
        for char in s:
            if char.isalpha() or char.isdigit():
                words.append(char.lower())

        reverse = words.copy()
        reverse.reverse()

        print(reverse)
        print(words)
      
        #return words == reverse

    story = "A man, a plan, a canal: Panama"
    story1 = "race a car"
    print(fn(story1))
