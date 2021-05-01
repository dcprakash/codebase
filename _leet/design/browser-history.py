"""
https://leetcode.com/problems/design-browser-history/

"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.page=[homepage]
        self.ix=0
        

    def visit(self, url: str) -> None:
        if self.ix==len(self.page)-1:
            self.page.append(url)
            self.ix+=1
            return
        
        # after hitting back button, if we visit then clear fwd history
        self.page[self.ix+1]=url
        self.ix+=1
        self.page=self.page[:self.ix+1]
        

    def back(self, steps: int) -> str:
        self.ix-=steps
        if self.ix<0:   self.ix=0
        return self.page[self.ix]
        

    def forward(self, steps: int) -> str:
        self.ix=min(len(self.page)-1, self.ix+steps)
        return self.page[self.ix]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
