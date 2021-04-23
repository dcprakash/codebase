# https://leetcode.com/problems/validate-ip-address/solution/

class Solution:
    def validate_ipv4(self, s):
        s=s.split(".")
        for i in s:
            if len(i) ==0 or len(i)>3:
                return "Neither"
            if not i.isdigit():
                return "Neither"
            if int(i)>255:
                return "Neither"
            if i[0]=='0' and len(i)!=1:
                return "Neither"
        return "IPv4"

    
    def validate_IPv6(self, s):
        s=s.split(":")
        hexdigits = '0123456789abcdefABCDEF'
        for i in s:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            # Check if all items in a list are True: all
            if len(i) == 0 or len(i) > 4 or not all(c in hexdigits for c in i):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, IP):
        if IP.count(".")==3:
            return self.validate_ipv4(IP)
        elif IP.count(":")==7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"

