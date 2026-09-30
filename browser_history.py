class Node:
    def __init__(self, val: str, prev: Node | None, next: Node | None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage, None, None)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        self.current.next = Node(url, self.current, None)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)