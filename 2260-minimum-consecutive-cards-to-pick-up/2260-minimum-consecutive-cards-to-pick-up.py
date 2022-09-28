class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        right = 0
        answer = 100001
        visited = set()
        while right < len(cards):
            if cards[right] not in visited:
                visited.add(cards[right])
                right += 1
            else:
                answer = min(answer, right-left+1)
                visited.remove(cards[left])
                left += 1

        if answer < 100001:
            return answer
        return -1