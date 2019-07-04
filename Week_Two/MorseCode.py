class Solution:
    def uniqueMorseRepresentations(self, words):
      morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
          "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."]

      words1 = 97
      morse_words = []
      count = []

      for word in words:
        letter = ""
        for char in word:
          letter += morse[ ord(char) - words1 ]

        morse_words.append(letter)

        if letter not in count:
          count.append(letter)

      return len(count)
