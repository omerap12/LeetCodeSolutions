# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

class Solution:
	def closeStrings(self, word1: str, word2: str) -> bool:
		"""
		Obeservation: two strings are close if and only if len(word1) == len(word2) and
		unique_char(word1) == unique_char(word2) and the values list of the chars at the two words are identical
		:param word1: First word
		:param word2: Second word
		:return: True if word1 is close to word2 else False
		"""
		if len(word1) != len(word2):
			return False
		unique_word_1 = set(word1)
		unique_word_2 = set(word2)
		if unique_word_1 != unique_word_2:
			return False
		values_dict_word_1 = {}
		values_dict_word_2 = {}
		for word in word1:
			if word in values_dict_word_1.keys():
				values_dict_word_1[word] += 1
			else:
				values_dict_word_1[word] = 1
		for word in word2:
			if word in values_dict_word_2.keys():
				values_dict_word_2[word] += 1
			else:
				values_dict_word_2[word] = 1
		return list(sorted(values_dict_word_1.values())) == list(sorted(values_dict_word_2.values()))
