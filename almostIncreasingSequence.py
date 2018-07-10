def almostIncreasingSequence(sequence):
	# c = 0
	# for i in range(len(sequence) - 1):
	# 	if sequence[i] >= sequence[i + 1]:
	# 		c += 1
	# return c < 2

	# miss = 0
	# # while True:
	# n = 0
	# for i in range(len(sequence) - 1):
	# 	if sequence[i] >= sequence[i + 1]:
	# 		# print('pop', sequence[i], 'at', i)
	# 		try:
	# 			valid = sequence[i - 1] < sequence[i + 1]
	# 		except IndexError:
	# 			valid == True
	# 		if valid:
	# 			del sequence[i]
	# 			print('del', sequence[i], 'at', i)
	# 		else:
	# 			try:
	# 				print('del', sequence[i + 1], 'at', i + 1)
	# 				del sequence[i + 1]
	# 			except IndexError:
	# 				pass

	# 		# miss += 1
	# 		break
	# 		print('sequence=',sequence)
	# r_seq = list(reversed(sequence))
	# print('r_seq=',r_seq)	
	# for i in range(len(r_seq) - 1):
	# 	if r_seq[i] <= r_seq[i + 1]:
	# 		return False
	# return True

	## Find our first potential trouble.
	start_i = 0
	# Iterate sequence til we find the index of the first element out of order. Initial solution skipped
	# this step and started from i = 0, which was too slow.
	for i in range(len(sequence) - 1):
		if sequence[i] >= sequence[i + 1]:
			start_i = i
	# Start checking subsequences, starting at index of first element out of order
	for i in range(start_i, len(sequence)):
		# Copy the sequence.
		sub_seq = sequence[:]
		# Delete element from subsequence at index for this pass
		del sub_seq[i]
		clean_pass = True
		# Check the subsequence from beginning to end for elements out of order.
		for n in range(len(sub_seq) - 1):
			# If we find an element out of order, this pass is dirty. No need to do more comparisons for this i.
			if sub_seq[n] >= sub_seq[n + 1]:
				clean_pass = False
				break
		# If we exit the trial loop for this value of i without clean_pass set to False, the trial sequence
		# is strictly increasing. Return True.
		if clean_pass:
			return True
	# If we get here, we tried every subsequence and none of them were strictly increasing. Return False.
	return False




def main():
	sequences = [[1,3,2,1],
				[1,3,2],
				[1,2,1,2],
				[1,4,10,4,2],
				[10,1,2,3,4,5],
				[1,1,1,2,3],
				]
	for sequence in sequences:
		print(almostIncreasingSequence(sequence))

if __name__ == "__main__":
	main()