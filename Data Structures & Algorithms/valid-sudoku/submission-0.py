class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True

        rows = []
        columns = []
        boxes = []

        for _ in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                b = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in columns[c] or value in boxes[b]:
                    isValid = False
                    break
                
                rows[r].add(value)
                columns[c].add(value)
                boxes[b].add(value)
        
        return isValid