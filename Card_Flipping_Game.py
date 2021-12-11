Solution To: https://leetcode.com/problems/card-flipping-game/

class Solution:
    def flipgame(self, fronts, backs):
        cards = zip(fronts, backs)  # create a list of cards (x,y) where x is front card value and y is back card value
        same_value = []  # list of cards with x == y
        possible_answer = []  # all other cards value
        for card in cards:  # iterating through the cards
            if card[0] == card[1]:
                same_value.append(card[0])

        for i in (fronts + backs):  # iterating through the values of both front and back
            if i not in same_value:
                possible_answer.append(i)

        if possible_answer:  # return the min, if empty return 0
            return min(possible_answer)
        return 0
