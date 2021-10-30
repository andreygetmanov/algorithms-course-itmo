
   
#Modules
import numpy as np
import matplotlib.pyplot as plt
import SA_anime as lib

#global variables
input_data = []


# instructions for the user
print("We are going to solve TSP(travelling salesman problem) using Simulated annealing and matplotlib library for better visualization of the algorithm")
print("Do you want to add your own file for inputs or let me create some random inputs")
print("press 1 for random otherwise enter your full file location")

s='./cities.txt'
n=0

if s=="1":
	# creating random inputs
	print("enter the amount of inputs (points/cities)")
	n=input()
	input_data=np.random.randint(1000,size=(n,2))
	
else:
	print("Input should be in the format as described in the Readme section")
	
	#fetching file from user's database
	with open(s) as f:
		for line in f:
			numbers_str = line.split()
			x=float(numbers_str[0])
			y=float(numbers_str[1])
			input_data.append((x,y))

final_arr = lib.sa_algorithm(input_data)
final_l = lib.total_length(final_arr,n)

print("minimum length using simulated annealing- ")
print(final_l)
print("\nfinal order of coordinates to visit for near optimal solution--\n")
print(final_arr)