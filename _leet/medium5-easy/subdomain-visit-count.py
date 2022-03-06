"""
https://leetcode.com/problems/subdomain-visit-count/

domain
subdomain

"""
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains):
        ans=Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count=int(count)
            subdomain=domain.split('.')
            for i in range(len(subdomain)):
                ans[".".join(subdomain[i:])]+=count
            # print(ans)      # Counter({'discuss.leetcode.com': 9001, 'leetcode.com': 9001, 'com': 9001})
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
            
        
obj=Solution()
print(obj.subdomainVisits(["9001 discuss.leetcode.com", "50 yahoo.com"]))