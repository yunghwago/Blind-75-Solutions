class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer, rightPointer = 0, 1
        output = 0
        currentProfit = 0
        while rightPointer < len(prices):
            if prices[rightPointer] - prices[leftPointer] < 0: #negative profit
                leftPointer = rightPointer
            elif prices[rightPointer] - prices[leftPointer] > 0: #positive profit
                currentProfit = prices[rightPointer] - prices[leftPointer]
                output = max(output, currentProfit)
            rightPointer += 1
        return output
