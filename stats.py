
def get_num_words(text):
	return len(text.split())

def character_count(text):
	count_dict = {}
	lowered_text =  str.lower(text)
	for char in lowered_text:
		if char in count_dict:
			count_dict[char] += 1
		else:
			 count_dict[char] = 1
	return count_dict
