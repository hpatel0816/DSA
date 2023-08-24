#LeetCode (1768 - Merge Strings Alternately)

#Prompt: Given 2 strings, return a merged string by adding their letters in alternating sequence

def mergeAlternately(word1, word2):
        merged_word = ""

        #Edge cases to handle empty strings
        if word1 == "":
            return word2
        elif word2 == "":
            return word1

        #Remove letters from both strings and add to merged string until the end of one string
        while len(word1) > 0 and len(word2) > 0:
            merged_word += word1[0]
            word1 = word1[1:]

            merged_word += word2[0]
            word2 = word2[1:]

        #Once we reach end of one string, add the remainder of second string to merged string
        if len(word1) == 0:
            merged_word += word2
        elif len(word2) == 0:
            merged_word += word1

        return merged_word


#Test Casses
assert mergeAlternately("abc", "pqr") == "apbqcr", "Solution: 'apbqcr'"
assert mergeAlternately("ab", "pqrs") == "apbqrs",  "Solution: 'apbqrs'"
assert mergeAlternately("abcd", "pq") == "apbqcd",  "Solution: 'apbqcd'"
assert mergeAlternately("", "abcd") == "abcd", "Solution: 'abcd'"
assert mergeAlternately("abc", "") == "abc", "Solution: 'abc'"
print("All tests passed.")
