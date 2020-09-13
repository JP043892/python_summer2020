# Graphically
import matplotlib.pyplot as plt
import math
import numpy as np
import array
import random
import datetime

# =============================================================================
# First I'll implement merge sort. This algorithm uses both recursive and non-recursive techniques.
# It is a stable, quasilinear algorithm.
# =============================================================================
test = [5, 8, 3, 9, 1, 2] # should yield [1, 2, 3, 5, 8, 9]
test2 = [2, 9, 8, 6, 7, 5, 3, 8] # should yield [2, 3, 5, 6, 7, 8, 8, 9]
# divides OG list into two halves, then divides those halves, THEN merges sorted halves
# Just a more complicated way of putting the elements in numerical order
def merge(A,B,compare):
	result = [] 
    # i represents the left half (A) and j represents the right half (B)
	i,j = 0,0
	while (i < len(A) and j < len(B)):
		if compare(A[i],B[j]): # if A[i] is greater, we add to the right half
			result.append(A[i])
			i += 1 
		else:
			result.append(B[j]) # if B[i] is greater, we add to the right half
			j += 1 #go through each element in B
	while (i < len(A)):
		result.append(A[i])
		i += 1 #go through each element in A
	while (j < len(B)):
		result.append(B[j])
		j += 1 #go through each element in B
	return result


def merge_sort(list, compare = lambda x, y: x < y):
     #Used lambda function to sort list in both(increasing and decresing) order.
     #By default it sorts array in increasing order
     #Divides list in half, then recursively halves and sorts based on value
     #until there are only two elements in each list.
	if len(list) < 2:
		return list[:]
	else:
		middle = len(list) // 2
		A = merge_sort(list[:middle], compare)
		B = merge_sort(list[middle:], compare)
		return merge(A, B, compare) #bring the sublists back together in numerical order

print(merge_sort(test))


# =============================================================================
# Next I'll implement insertion sort. This is a non-recursive, stable algorithm.
# According to https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/
# This sorting algorithm is best for small lists
# Because my list is not already sorted, the complexity is quadratic time 
# =============================================================================
# Start by defining my list to sort:
test = [1, 9, 5, 7]
test2 = [10,1,5,0,6,8,7,3,11,4]
def insertion_sort(list):
    # we start with a key 
    i=1
    while(i<len(list)):
      element=list[i] #the element is the ith number within th elist
      j=i
      i=i+1 # we compare our key with the previous element
    
    #if the element is greater than the key, the element moves to the right
      while(j>0 and list[j-1]>element): 
        list[j]=list[j-1]
        j=j-1
    
      list[j]=element
    
    i=0
    while(i<len(list)): #displays our newly sorted list
      print (list[i])
      i=i+1
# function should return numbers sorted least to greatest
insertion_sort(test) # 1, 5, 7, 9
insertion_sort(test2) # 0, 1, 3, 4, 5, 6, 7, 8, 10, 11

# =============================================================================
# Finally I will run a simulation and graph the results for both algorithms
# =============================================================================

# Start by generating a random list. I will nest this in a function.
def simulate(N):
    sim_list = []
    for i in range(0,150):
        samp = random.sample(range(0,1000), N)
        sim_list.append(samp)
    return sim_list
#simulate(10)[1]

# Now that I have my simulation data, I need to father the runtime data in a function
def time_calc(N):
    merge_time = [] #all the run times for merge_sort
    ins_time = [] #all the run times for insertion_sort
    sim_list = simulate(N) #my simulation list
    
    for i in range(0, 150):
        start_time = datetime.datetime.now() #gives me the time before running algorithm
        merge_sort(sim_list[i]) #run merge_sort on each list within my simulation list
        end_time = datetime.datetime.now() - start_time ##total run time
        merge_time.append(end_time.microseconds) # add runtimes to empty list
    
        start_time = datetime.datetime.now() #gives me the time before running algorithm
        insertion_sort(sim_list[i]) #run insertion sort on each list within my simulation list
        end_time = datetime.datetime.now() - start_time #total run time
        ins_time.append(end_time.microseconds) # add runtimes to empty list

    return [merge_time, ins_time]

# Here I tested my functions to determine what the data looks ike
# This helps me to better simulate later for the plot
np.mean(time_calc(1000)[1])
print(merge_time) #these times are super fast. 
# ^ I should expect this plot to therefore be pretty steady
print(ins_time) # this plot will show a greater increase
time_calc(10)


# Now I generate x and y values for my plot
x = list(range(1,601)) #first generate a random list of x values
merge_mean = []
ins_mean = []

# I then iterate over these x-values to find the average y-value(runtime) for each algorithm
for i in x:
   # first run the time calc function for all values of x
   # for each sublist of the merge sort run times, I grab the mean
   get_means = np.mean(time_calc(i)[0])
   # I then add all the means for each x value to the merge means list
   merge_mean.append(get_means)
   # same process for insertion mean
   get_means2 = np.mean(time_calc(i)[1]) 
   ins_mean.append(get_means2)

  
plt.plot(x, ins_mean, 'g-', label = "Insertion Sort")
plt.plot(x, merge_mean, 'b-', label = "Merge Sort")
plt.xlabel('N')
plt.ylabel('Avg. Sorting Runtime')
plt.legend()
plt.show()

# =============================================================================
# Sources used:
# https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/
# https://www.pythonpool.com/insertion-sort-python/#:~:text=%20Algorithm%20For%20Python%20Insertion%20Sort%20%201,the%20value%20at%20the%20correct%20position.%20More%20
# https://www.educba.com/sorting-algorithms-in-python/
# https://www.kite.com/python/docs/datetime.datetime.time
# =============================================================================
    