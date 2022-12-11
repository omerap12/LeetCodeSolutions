class Solution:
    def dividePlayers(self, skill):
        """
        To have the same chimesty in all teams get the best player to be with
        the worst player and so on
        """
        skill.sort()
        res = 0
        left_ptr = 0
        right_ptr = len(skill)-1
        chemistry = skill[left_ptr]+skill[right_ptr]
        while left_ptr < right_ptr:
            if skill[right_ptr]+skill[left_ptr] != chemistry:
                return -1
            res += skill[left_ptr]*skill[right_ptr]
            left_ptr += 1
            right_ptr -= 1
        return res
