'''
Created on Oct 4, 2018

@author: daduva
'''
######################################################################################################
# NOTE: READ THIS BEFORE CONTINUING

# Below is a tester file for the perform_calc.py program. I have commented out most of the functions,
# because if I had left them all uncommented they would all run at the same time, and there would have
# been too much output. Because of this, I am leaving it up to you (the user) to uncomment parts of 
# this program and explore the features it has to offer. Feel free to try it out and if you have any
# questions, shoot me an email at dduval6@outlook.com
######################################################################################################


from perform_calc import *

################### Input Function ######################

first_func = Calculus('(3*x^3-4)/(4*x^4)')


################### Set Domain ##########################

first_func.set_domain(list(range(-50, 50)))

################### Set Range ###########################

first_func.set_range()

########### Take Integrals/Derivatives ##################

#print(first_func.take_derivative())
#print(first_func.take_integral())

################### Check Object Dictionary to ensure everything has been set up properly ##########################

#print(first_func.__dict__)


########### Plot Points of Regular Function ##############

first_func.plot_points()


############ Plot Points of Derivative Function ##########

#first_func.plot_derivative()

