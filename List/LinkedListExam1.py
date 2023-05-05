#인터넷 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class 를 구현 할 것이다.
#구현할 브라우저는 homepage에서 시작하고, 이후 다른 url에 방문할 수 있따.
# 뒤로가기와 앞으로가기가 작동하도록 구현하라

#ex browserHistory = BrowserHsitory("leetcode.com")


class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
       self.head = self.current = ListNode(val=homepage)

    def visit (self,url):
        self.current.next = ListNode(val=url , prev=self.current)
        self.current= self.current.next
        return print(None)  
    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return print(self.current.val)
    def forword(self, steps):
        while steps > 0 and self.current.next != None:
            steps -=1
            self.current = self.current.next
        return print(self.current.val)
    


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forword(1)
browserHistory.visit('linkedin.com')
browserHistory.forword(2)
browserHistory.back(2)
browserHistory.back(7)    