'''
https://leetcode.com/problems/encode-and-decode-strings/

strs[i] contains any possible characters out of 256 valid ASCII characters.
Seems like one has to use non-ASCII unichar character, for example unichr(257) in Python

'''

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s)}:{s}' for s in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        i = 0
        out = []
        while i < len(s):
            colon = s.index(':', i)     # string.index(value, start, end)
            count = int(s[i:colon])     # get first int value i.e., 5
            out.append(s[colon + 1:colon + 1 + count])
            i = colon + count + 1
        return out
        
s=Codec()
print(s.encode(["Hello","Worlds"]))
print(s.decode("5:Hello6:Worlds"))
