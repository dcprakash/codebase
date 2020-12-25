# Python 3 program to find minimum
# number of characters
# to be removed to make two
# strings anagram.

CHARS = 26


# function to calculate minimum numbers of characters to be removed to make two strings anagram
def remAnagram(str1, str2):
    # make hash array for both string
    # and calculate
    # frequency of each character
    count1 = [0] * CHARS
    count2 = [0] * CHARS

    # count frequency of each character
    # in first string
    i = 0
    while i < len(str1):
        count1[ord(str1[i]) - ord('a')] += 1
        i += 1

    # count frequency of each character
    # in second string
    i = 0
    while i < len(str2):
        count2[ord(str2[i]) - ord('a')] += 1
        i += 1

    print(count1)
    print(count2)

    # traverse count arrays to find
    # number of characters
    # to be removed
    result = 0
    for i in range(26):
        result += abs(count1[i] - count2[i])
    return result


# Driver program to run the case
if __name__ == "__main__":
    str1 = "bcadeh"
    str2 = "hea"
    print(remAnagram(str1, str2))

# The ord() method returns an integer representing the Unicode code point of the given Unicode character.
# ChitraNayal
