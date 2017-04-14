##similarity determines the similarity between two strings.

#assuming the two titles are similar in length and such
def similarity(first, second):
	length1 = len(first)
	length2 = len(second)
	if length1 == 0 or length2 == 0: 
		return 1

	if length1 > length2:
		length = length2
	else:
		length = length1
	similarityCount = 0
	for i in range(0, length):
		if first[i] == second[i]:
			similarityCount += 1
		elif first[i].lower() == second[i].lower():
			# similarityCount += 0.8
			similarityCount+=1 #assuming smaller letters don't mean anything

	return float(similarityCount)/length


if __name__ == '__main__':
	print "determine the similarity of two words."
	first = raw_input("what is the first word? ")
	second = raw_input("what is the second word? ")
	print "the similarity =", similarity(first, second)