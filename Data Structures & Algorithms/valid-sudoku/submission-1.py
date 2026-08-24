class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidSequence(row):
                return False

        for i in range(len(board)):
            col = [row[i] for row in board]

            if not self.isValidSequence(col):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                
                if not self.isValidSequence(box):
                    return False

        return True

    def isValidSequence(self, sequence: List[str]) -> bool:
        seen = set()

        for s in sequence:
            if s == ".":
                continue

            if s in seen:
                return False

            seen.add(s)

        return True
