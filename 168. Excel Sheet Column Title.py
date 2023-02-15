class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = []
        while columnNumber > 0:

            result.append(chr(65 + (columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        result.reverse()
        return "".join(result)
