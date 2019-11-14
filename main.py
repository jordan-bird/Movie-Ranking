import os
import re
from py3votecore.schulze_method import SchulzeMethod
from py3votecore.condorcet import CondorcetHelper
from time import sleep

def vote(ballots):
	output = SchulzeMethod(ballots, ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict()
	if 'tied_winners' in output.keys():
		#print(output['tied_winners'])
		return output['tied_winners']
	return output['winner']

def getBallots(removeWinners=""):
	lists = []
	ballots = []
	for filename in os.listdir(os.path.join(dir_path)):
		f = open((dir_path + filename), "r")
		processingList = {'count':1}
		movies = []
		line = f.readline()
		lines=[]
		while line:
			line = line.strip('\n')
			line = line.replace(' ', '')
			line = line.replace(':', '')
			line = line.replace('-', '')
			line = line.replace(',', '')
			line = line.lower()
			if(removeWinners.count(line)==0):
				movies.append([line])
			line = f.readline()
		f.close()
		processingList['ballot'] = movies
		ballots.append(processingList)
	return ballots
	

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '\lists\\'
print("Getting lists from: " + dir_path + "\n")
num_files = len([f for f in os.listdir(dir_path)if os.path.isfile(os.path.join(dir_path, f))])
print("There are " + str(num_files) + " lists!")


print("\nBegin voting...\n")

winners=[]
for x in range(0, 25):
	if(x==0):
		ballots = getBallots()
	else:
		ballots = getBallots(winners)
	winner = vote(ballots)
	print(str(x+1) + ": " + str(winner))
	
	#print(type(winner))
	
	if type(winner) is set:
		for val in winner:
			winners.append(val)
	else:
		winners.append(winner)
		
	
	
