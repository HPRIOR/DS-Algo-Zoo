'''

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" = true
'''


def exists(board, word):
    directions = [(0, 1), (0, -1), (1, 0)]

    def helper(current_word: str, d):
        if current_word == "":
            return True

        if current_word.startswith(board[d[0]][d[1]]):
            for direct in directions:
                new_direction = (direct[0] + d[0], direct[1] + d[1])
                if helper(current_word[1:], new_direction):
                    return True

        return False

    return helper(word, (0, 0))


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exists(board, word))
