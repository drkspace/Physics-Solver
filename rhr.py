#(c) Daniel Robert Kramer, All Rights Reserved
import math

#Dictonary for converting the entry of the user to a vector
vectors = {'1': [0,1,0],'2': [0,-1,0],'3': [-1,0,0],'4': [1,0,0],'5': [0,0,1],'6': [0,0,-1]}

#Dictonary for converting vectors to english meanings
vector_to_english = {'[0, 1, 0]': 'Out of the page', '[0, -1, 0]': 'Into the page', '[-1, 0, 0]': 'To the Left', '[1, 0, 0]': 'To the Right', '[0, 0, 1]': 'Upwards', '[0, 0, -1]': 'Downwards', '[0, 0, 0]': 'No Force'}

#What the user will check off for the direction of the thing they are using
printout_list = ["Out of the page","Into the page","To the left","To the right","Upwards","Downwards"]
printout_list_2 = ["Above","Below","To the left","To the right","In front of","Behind"]
printout_list_3 = ["Increasing","Decreasing","Not Changing"]

#All the negative vectors
negative=['[-1, 0, 0]','[0, -1, 0]','[0, 0, -1]']

#Method for finding a cross product between 2 vectors
def cross_product(a,b):

	c = [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
	return c

#Method for finding the direction of the force on a particle given a field and velocity
def rhr_field(B=None, V=None):

	#For use if done though a command line
	if B is None:
		print "Magnetic Field Direction"
		for i in printout_list:
			print i
		B=int(input())
	

	#For use if done though a command line
	if V is None:
		print "Velocity"
		for i in printout_list:
			print i

		V=int(input())

	#Converting user input to vectors
	vB=vectors[str(B)]
	vV=vectors[str(V)]

	#Get the cross product of the reulting vectors
	result = cross_product(vB,vV)

	return result

#Method for finding the direction of the magnetic field given a current direction and point location
def rhr_current(I=None, P=None):
	
	#For use if done though a command line
	if I is None:
		print "Current Direction"
		for i in printout_list:
			print i
		I=int(input())
	
	
	#For use if done though a command line
	if P is None:
		print "point location"
		for i in printout_list_2:
			print i

		P=int(input())

	#Converting user input to vectors
	vI=vectors[str(I)]
	vP=vectors[str(P)]

	#Get the cross product of the reulting vectors
	result = cross_product(vI,vP)

	return result

#Method for finding the resulting current direction from a field, change in field and area
def induced_current(B=None, dB=None, dA=None):

	#For use if done though a command line
	if B is None:
		print "Magnetic Field Direction"
		for i in printout_list:
			print i
		B=int(input())
	
	#For use if done though a command line
	if dB is None:
		print "Is the field increasing, decreasing, or neither?"
		print "1-increasing"
		print "2-Decreasing"
		print "3-Not changing"
		dB=int(input())	

	#For use if done though a command line
	if dA is None:
		print "Is the area inside the field increasing, decreasing, or neither"
		print "1-increasing"
		print "2-Decreasing"
		print "3-Not changing"
		dA = int(input())

	#Converting the direction of the field to a vector
	vB=str(vectors[str(B)])
	
	#If the field and area are not changing
	if dB == dA and dB == 3:
		return "No induced current"

	#If one of them are decreasing and the other isn't increasing
	elif (dB == dA and dB == 2) or (dB==3 and dA==2) or (dA==3 and dB==2):
		direction = "Clockwise"
		if vB not in negative:
			direction = "Counterclockwise"

		return "The current is going {}".format(direction)
	
	#If one of them are increasing and the other isn't decresing
	elif (dB == dA and dB == 1) or (dB==3 and dA==1) or (dA==3 and dB==1):

		direction = "Clockwise"
		if vB in negative:
		
			direction = "Counterclockwise"

		return "The current is going {}".format(direction)

	#If neither are the same and not not changing
	else:
		return "Indeterminate. Further calculations needed"
