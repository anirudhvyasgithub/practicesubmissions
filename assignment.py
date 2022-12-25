#Importing required functions and libraries
from itertools import permutations 
import re

#Function to check invalid sequnces like ++, --

def generate_invalid_operations(seq):    
  # Get all permutations of length 2 
  # and length 2 
  perm = permutations(['+', '*', '-','/','%'], 2) 
  comb_list = []
  # Print the obtained permutations 
  for i in list(perm): 
      comb_list.append((i[0]+i[1])) 
  seq_list =  comb_list + ['++','--']
  #Creating result flag to check output
  res_var = 0
  for i in seq_list:
    if(seq.find(i)!= -1):
      res_var = 1
      break
    else:
      pass

  return res_var

def calc_checker(seq):

  try:

    #Splitting based on delimiter
    test = seq.split('?')
    #Rule based sequence evaluation
    for i in range(0,len(test)):
      element = str(test[i])
      if(i == 0 and generate_invalid_operations(test[0]) !=1 and  test[i]!=''):
        print(eval(test[0]))
        res_set = test[0]
      elif(i == 0 and generate_invalid_operations(test[0]) ==1):
        print('ERROR')
        break
      elif(i != 0 and generate_invalid_operations(test[i]) !=1 and test[i]!=''):
        print(eval(res_set+str(test[i])))
        res_set = str((res_set+str(test[i])))
      elif(i != 0 and generate_invalid_operations(test[i]) ==1):
        print('ERROR')
        break

  except:

    print('Please check input sequence')

#Object to accept input sequence and return result set
calc_checker(str(input('Enter  Sequence')))
