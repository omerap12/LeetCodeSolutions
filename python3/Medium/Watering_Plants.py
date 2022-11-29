Solution To: https://leetcode.com/problems/watering-plants/

class Solution(object):
    def wateringPlants(self, plants, capacity):
        current_water_sum = capacity  # saving the current water supply
        moves_count = 0
        current_index = -1
        river_check = False  # mark if the last visit was to the river

        while True:
            if current_index + 1 == len(plants):  # if were at the end return moves count
                return moves_count
            elif plants[current_index + 1] <= current_water_sum:  # means we have enough water to fill the plants
                current_water_sum -= plants[current_index + 1]  # sub water supply 
                if river_check:  # if we visited the river at the last iteration add the distance from the river to 
                    # our current moves counter 
                    moves_count += current_index + 1
                moves_count += 1
                current_index += 1
                river_check = False  # mark that were not at the river now
            else:
                moves_count += current_index + 1  # go back to river
                river_check = True  # mark that were at the river
                current_water_sum = capacity  # fill water
