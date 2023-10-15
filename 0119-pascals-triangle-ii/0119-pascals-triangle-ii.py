class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        if rowIndex > 0:
            for i in range(1, rowIndex+1):
                temp = [0] + res[-1] + [0]
                res.append([temp[x] + temp[x+1] for x in range(i+1)])
                
        return res[-1]