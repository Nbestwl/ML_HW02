__authors__ = 'Casey Sader and Lei Wang'

import sys
import os
import string
import pickle

def calculateProbabilities(training_data_file):
	"""
	This is a dictionary containing all of the words that could be first in a line
	and the number of times they are first
	"""
	first_words = {}

	"""
	This is a dictionary containing every word, and a list of the words
	that could come after them (including '' which means the line ends)
	"""
	next_words = {}

	num_first_words = 0

	# loop through every line in the file
	for line in open(training_data_file):
		# if not blank line then edit dictionary for each word
		if line.strip():
			# remove punctuation and split into individual words
			table = string.maketrans("","")
			line = line.translate(table, string.punctuation).lower()
			words = line.split()

			# go through each word in the line and add to dictionary
			for i in range(0,len(words)):
				# first word
				if i == 0:
					# add to as a possible first word and increase count
					if words[i] not in first_words:
						first_words[words[i]] = 1
					else:
						first_words[words[i]] = first_words[words[i]] + 1
					num_first_words+=1

				# add posible next words for our word
				if words[i] not in next_words:
					# check if there is a next word
					if (i+1) < len(words):
						next_words[words[i]] = [words[i+1]]
					else:
						next_words[words[i]] = ['']
				else:
					# check if there is a next word
					if (i+1) < len(words):
						next_words[words[i]].append(words[i+1])
					else:
						next_words[words[i]].append('')

	next_words[''] = []
	states = next_words.keys()

	for key in first_words:
		first_words[key]/=float(num_first_words)

	next_words_freq = {}

	for state in states:
		transition_probs = {}
		for pos_next in states:
			if next_words[state].count(pos_next) != 0:
				transition_probs[pos_next] = next_words[state].count(pos_next)/float(len(next_words[state]))
		next_words_freq[state] = transition_probs

	return states, first_words, next_words_freq

def main(args):
	training_data_file = args[0]
	states, first_words_freq, next_words_freq = calculateProbabilities(training_data_file)

	cwd = os.getcwd()

	if not os.path.exists(cwd + '/pickled'):
		os.makedirs(cwd + '/pickled')

	with open(cwd + '/pickled/states.pkl', 'wb') as file:
		pickle.dump(states, file, protocol=pickle.HIGHEST_PROTOCOL)

	file.close()

	with open(cwd + '/pickled/first_words_freq.pkl', 'wb') as file:
		pickle.dump(first_words_freq, file, protocol=pickle.HIGHEST_PROTOCOL)

	file.close()

	with open(cwd + '/pickled/next_words_freq.pkl', 'wb') as file:
		pickle.dump(next_words_freq, file, protocol=pickle.HIGHEST_PROTOCOL)

	file.close()

if __name__ == "__main__":
	main(sys.argv[1:])
