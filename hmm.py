'''
Author: Lei Wang, Casey Sader
Date: 03/25/2019
'''

import operator
import random as rand
import pickle
import sys


def read_pickle(file):
	dic = {}
	with open(file, 'rb') as handle:
		dic = pickle.load(handle)

	handle.close()
	return dic


def possible_state(state):
	totals = []
	running_total = 0

	for w in state.values():
		running_total += w
		totals.append(running_total)

	rnd = rand.random() * running_total
	for i, total in enumerate(totals):
		if rnd < total:
			keys = state.keys()
			return keys[i]


def hmm(states, init_states, trans_prob, sequence, cur_state=None, init=True):
	if cur_state == '':
		return sequence
	else:
		if init:
			cur_state = possible_state(init_states)

		sequence.append(cur_state)
		next_state = possible_state(trans_prob[cur_state])
		hmm(states, init_states, trans_prob, sequence, cur_state=next_state, init=False)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'incorrect parameters, please check readme file'
	else:
		option = sys.argv[1]

		sequence = []
		states = read_pickle('pickled/states.pkl')
		start_p = read_pickle('pickled/first_words_freq.pkl')
		trans_p = read_pickle('pickled/next_words_freq.pkl')

		if option == '-g':
			hmm(states, start_p, trans_p, sequence)
			print ' '.join(sequence)
		elif option == '-p':
			sentence = raw_input('Please enter a sentence to be predicted:\n')
			last_word = sentence.split()[-1]
			predict_start = {}

			if last_word not in states:
				print 'warning: word not found in training set'
			else:
				for state in states:
					predict_start[state] = 0.0
				predict_start[last_word] = 1.0
				hmm(states, predict_start, trans_p, sequence)
				print ' '.join(sequence[1:])
		else:
			print 'please input a option'
