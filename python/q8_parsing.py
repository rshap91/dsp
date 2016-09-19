#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
import numpy as np
import pandas as pd
# w pandas
def pandas_way():
  df = pd.read_csv('football.csv')
  df['Goal_Ratio'] = df['Goals'] - df['Goals Allowed']
  print df.loc[df.Goal_Ratio == df.Goal_Ratio.apply(np.abs).max()]

# w csv
def csv_way():
  with open('football.csv', 'r+') as fhand:
    reader = csv.reader(fhand)
    data = [row for row in reader][1:] # get rid of header row
    goal_ratios = {r[0]: int(r[5]) - int(r[6]) for r in data}
    print sorted(goal_ratios.items(), reverse = True, key = lambda t: np.abs(t[1]))[0]
    
