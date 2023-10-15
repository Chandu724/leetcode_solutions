class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows > 1:
            for i in range(1, numRows):
                temp = [0] + res[-1] + [0]
                res.append([temp[x] + temp[x+1] for x in range(i+1)])
                
        return res
