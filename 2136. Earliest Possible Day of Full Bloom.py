class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:



        pots, length = [], len(plantTime)

        for index in range(length):

            plant = plantTime[index]
            grow = growTime[index]

            pots.append([plant, grow])

        pots = sorted(pots, key = lambda x:x[1], reverse = True)

        current_day = 0
        result = 0

        for pot in pots:

            current_plant , current_grow = pot

            current_day = current_day + current_plant

            result = max(result, current_day + current_grow)

        return result
