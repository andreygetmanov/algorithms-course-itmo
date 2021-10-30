# Modules

import math
import numpy as np
import matplotlib.pyplot as plt
global image_no

# calulate length between two points

def length (n1,n2):
	return math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)


# calculate total length to traverse all points

def total_length(arr,n):
	l=length(arr[0],arr[n-1])
	for i in range(n-1):
		l+= length(arr[i],arr[i+1])
	return l


# two_opt optimization for simulated annealing, using a random probabilty function to do selection

def two_opt_optimization(sol_arr,t,n,min_l):

	# picking two pair of consecutive integers, making sure they are not same
	ai = np.random.randint(0,n)
	bi = (ai+1)%n
	ci = np.random.randint(0,n)
	di = (ci+1)%n
	ai_,bi_,ci_,di_=ai,bi,ci,di

	if ai != ci and bi != ci:
		a =sol_arr[ai]
		b =sol_arr[bi]
		c =sol_arr[ci]
		d =sol_arr[di]

		# old lengths
		ab =length(a,b)
		cd =length(c,d)

		# new lengths, if accepted by our probability function
		ac =length(a,c)
		bd =length(b,d)

		diff = ( ab + cd ) - ( ac + bd )

		p = 0
		# for negative diff-> we'll use boltzman probabilty distribution equation-> P(E)=exp(-E/kT)
		if diff < 0:
			# k is considered to be 1
			p = math.exp( diff/t )

		# we'll sometimes skip the good solution
		elif diff > 0.05 :
			p = 1

		#print p
		if(np.random.random() < p ):

			new_arr = [x for x in range(0, n)]

			new_arr[0]=sol_arr[ai]
			i = 1

			while bi!= ci:

				new_arr[i]=sol_arr[ci]
				i = i+1
				ci = (ci-1)%n

			new_arr[i]=sol_arr[bi]
			i = i+1

			while ai!= di:
				new_arr[i] =sol_arr[di]
				i = i+1
				di =(di+1)%n


			# animate this frame
			frame_arr=new_arr
			frame_arr=np.array(new_arr)

			plt.ylim(-100,1100)
			plt.xlim(-100,1100)
			plt.axis('off')
			plt.scatter(frame_arr[:,0],frame_arr[:,1],color='g',s=50)
			plt.scatter([sol_arr[ai_][0],sol_arr[bi_][0],sol_arr[ci_][0],sol_arr[di_][0]],[sol_arr[ai_][1],sol_arr[bi_][1],sol_arr[ci_][1],sol_arr[di_][1]],color='r',s=75)
			plt.plot(frame_arr[:,0],frame_arr[:,1],color='b')
			plt.plot([frame_arr[0][0],frame_arr[-1][0]],[frame_arr[0][1],frame_arr[-1][1]], color='b')
			plt.title('Travelling Salesman Problem\n points ' + ("%d" % n) +' temp=' + ("%f" % t) + '    ' 'curr Length='+ ("%f" % (min_l-diff)))

			global image_no
			plt.savefig( ("%05d" % image_no) + '.png')
			image_no += 1
			plt.clf()

			return new_arr

	return sol_arr


# Simmulated Annealing algorithm----------------------------------------------	

def sa_algorithm (input_data):

	#length of input_data
	n=len(input_data)

	#creating a base solution
	sol_arr=input_data

	global image_no
	image_no = 1
	plt.clf()
	plt.title('Travelling Salesman Problem\n')
	#plt.axes([-10,1010,-10,1010])
	plt.ylim(-100,200)
	plt.xlim(-100,200)
	plt.axis('off')

	#plotting base solution
	for i in range(n):
		plt.scatter(sol_arr[i][0],sol_arr[i][1],color='g',s=50)
		plt.savefig( ("%05d" % image_no) + '.png')
		image_no += 1

	for i in range(n):
		plt.plot( [sol_arr[i][0],sol_arr[(i+1)%n][0]], [sol_arr[i][1],sol_arr[(i+1)%n][1]], color='b')
		plt.savefig( ("%05d" % image_no) + '.png')
		image_no += 1

	#plt.show()
	plt.clf()


	#initial temperature
	t = 100

	#current length
	min_l=total_length(sol_arr,n)
	print(min_l)

	i=0
	best_arr=[]

	while t>0.1:

		i= i+1

		#two_opt method- for optimization
		sol_arr=two_opt_optimization(sol_arr,t,n,min_l)

		#after 200 steps restart the process until the temperature is less than 0.1
		if i>=25 :

			i=0
			current_l=total_length(sol_arr,n)

			#because input size is approx. 200 i'm keeping the cooling schedule slow
			#t =t*0.9995
			#t =t*0.9
			t -=0.9
			#print t

			if current_l < min_l:
				print(current_l)
				min_l=current_l
				best_arr=sol_arr[:]

	return best_arr








