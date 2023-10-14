class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        
        for i in range(n):
            temp = [x for x in board[i] if x!="."]
            if len(set(temp)) < len(temp):
                return False

            temp = [x[i] for x in board if x[i]!="."]
            if len(set(temp)) < len(temp):
                return False
            
            
        for i in range(3):
            for j in range(3):
                temp = [x for x in board[i*3][j*3:j*3+3]+
                        board[i*3+1][j*3:j*3+3]+
                        board[i*3+2][j*3:j*3+3] if x!="."]
                if len(set(temp)) < len(temp):
                    return False
                
            

        return True