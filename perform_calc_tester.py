'''
Created on Oct 4, 2018

@author: daduva
'''
######################################################################################################
''' NOTE: READ THIS BEFORE CONTINUING

 Below is a tester file for the perform_calc.py program. I have commented out most of the functions,
 because if I had left them all uncommented they would all run at the same time, and there would have
 been too much output. Because of this, I am leaving it up to you (the user) to uncomment parts of 
 this program and explore the features it has to offer. Feel free to try it out and if you have any
 questions, shoot me an email at dduval6@outlook.com'''
######################################################################################################


from perform_calc import *

''' Input Function '''
x = Symbol('x') # Remember to include this every time at the top of your file.
                # If you don't, the Calculus Object below will have error messages.
 
first_func = Calculus(x**2-1)

''' Set Domain '''
first_func.set_domain(list(range(-10, 10)))
x_list = first_func.get_domain()
# print(x_list)

''' Set Range '''
y_list = first_func.set_range()
# print(y_list)

''' Take Integrals/Derivatives '''
# print(first_func.take_derivative())
# print(first_func.take_integral())

''' Check Object Dictionary to ensure everything has been set up properly '''
# print(first_func.__dict__)

''' Plot Points of Regular Function '''
# first_func.plot_points()

''' Plot Points of Derivative Function '''
# 
# first_func.plot_derivative()

''' Plot Points of Integral Functions '''
# print('\n\nPlotting the integral...')
# first_func.plot_integral()
# print('The integral function: '+first_func.take_integral())


''' Take a second or third Integral/Derivative '''
# print('\n\nTaking a second integral...')
# print('Original '+str(first_func))
# test = first_func.take_integral()
# integral_of_first_func = Calculus(test)
# print('1st Integral '+str(integral_of_first_func))
# second_integral = integral_of_first_func.take_integral()
# integral_two = Calculus(second_integral)
# print('2nd Integral '+str(integral_two))

''' Set the equation equal to zero and solve for a variable '''
# print(first_func.solvex(3))

''' __repr__, __str__, __add__ '''
# print('__str__ representation: '+str(first_func))
# print('__repr__ representation: '+repr(first_func))
# second_func = Calculus('2x^2')
# third_func = first_func + second_func
# print('adding two Calculus() objects together: '+third_func)
