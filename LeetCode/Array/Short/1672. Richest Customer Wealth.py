#1672. Richest Customer Wealth
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        high=0
        for i in range(len(accounts)):
            sum=0
            for j in accounts[i]:
                sum+=j
            high=max(high,sum)
        return high
