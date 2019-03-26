# Authors:
### Casey Sader & Lei Wang

# How to run the program:
### your system needs to support python2.7 before compile
### command to generate pickle files (optional, not recommended):
#### creates pickle files for state, transitional probability and initial state probability. It is not recommmended due to a long time to finish and it is done for your convenience.
```python
python parser.py ./shakespeare-plays/alllines.txt
```

### command to generate run
1. Generate new text from the text corpus:
```python
hmm.py -g
```
2. Perform text prediction given a sequence of words:
```python
hmm.py -p
```
3. Enter a sentence you desire, then it will output a prediction.

# Datasets:
1. [shakespeare-plays/alllines.txt](https://www.kaggle.com/kingburrito666/shakespeare-plays)

# Processes:
1. The text file is preprocessed and read in line by line.
2. The list is created containing all unique words from the text. This represents all possible states.
3. The dictionary then is created for initial state as well as the state probability.
4. Then the dictionary for the next word probability frequency is calculated. This represents the transition matrix. All end of lines are stored as ''.
5. All the dictionaries and matrix are store as pickle files for easy access.
6. Then the pickle files are read in and fed into the hmm function recursively to find the best fit based on its initial states and transition probabily matrix.

# Reference:
[Hidden Markov model wiki](https://en.wikipedia.org/wiki/Hidden_Markov_model)
