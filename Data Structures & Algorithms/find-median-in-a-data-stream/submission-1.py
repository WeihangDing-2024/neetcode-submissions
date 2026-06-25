class MedianFinder:

    def __init__(self):
        self.lower = [] # max heap
        self.higher = [] # min heap
        

    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush_max(self.lower, num)
            return
        if len(self.lower) > len(self.higher):
            if num > self.lower[0]:
                heapq.heappush(self.higher, num)
            else:
                heapq.heappush_max(self.lower, num)
                heapq.heappush(self.higher, heapq.heappop_max(self.lower))
        else:
            if num < self.higher[0]:
                heapq.heappush_max(self.lower, num)
            else:
                heapq.heappush(self.higher, num)
                heapq.heappush_max(self.lower, heapq.heappop(self.higher))
        # print(f"add num {num}, lower {self.lower}, higher {self.higher}")

    def findMedian(self) -> float:
        if len(self.lower) == len(self.higher):
            return (self.lower[0] + self.higher[0]) / 2
        else:
            return self.lower[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()