'''
Created on Oct 3, 2018

@author: daduva
'''
from sympy import Symbol, Derivative, integrate
import math
import plotly.offline as ply 
import plotly.graph_objs as go
x = Symbol('x')
class Calculus:
    def __init__(self, function):
        self.function = function
        self.x_values = []
        self.y_values = []
    def take_derivative(self):
        deriv= Derivative(self.function, x)
        return deriv.doit()
    def take_integral(self):
        integral = integrate(self.function, x)
        return integral.doit()
    def definite_integral(self, *args):
        return integrate(self.function, (x, args))
    def set_domain(self, range):
        self.x_values = range     
    def set_range(self):
        temp_yvals = [self.function.subs(x,xval) for xval in self.x_values]
        self.y_values = [int(item) for item in temp_yvals]
    def get_domain(self):
        return self.x_values
    def get_range(self):
        return self.y_values
    def plot_points(self):
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Plot 1'
        )
        data = [trace]
        try:
            ply.plot(data, filename = 'function-plot.html')
        except:
            print('An error occurred, or our function is Undefined. Please try again.')
    def plot_derivative(self):
        derivative_function = self.take_derivative()
        yval_temp = [derivative_function.subs(x,xval) for xval in self.x_values]
        derivative_yrange =  [int(item) for item in yval_temp]
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Original Function'
        )
        trace2 = go.Scatter(
            x = self.x_values,
            y = derivative_yrange,
            mode = 'lines',
            name = 'Derivative Function'
        )
        data = [trace, trace2]
        try:
            ply.plot(data, filename = 'function-plot.html')
        except:
            print('An error occurred, or our function is Undefined. Please try again.')
    def plot_integral(self):
        integral_function = self.take_integral()
        yval_temp = [integral_function.subs(x,xval) for xval in self.x_values]
        integral_yrange = [int(item) for item in yval_temp]
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Original Function'
        )
        trace2 = go.Scatter(
            x = self.x_values,
            y = integral_yrange,
            mode = 'lines',
            name = 'integral Function'
        )
        data = [trace, trace2]
        try:
            ply.plot(data, filename = 'function-plot.html')
        except:
            print('An error occurred, or our function is Undefined. Please try again.')
    def solvex(self, variable):
        return self.function.subs(x,variable)    
    def __repr__(self):
        return "Calculus('{}')".format(self.function)
    def __str__(self):
        return "Function: {}".format(self.function)  
    def __add__(self, other):
        return self.function + ' + ' + other.function

######################################################################################################
'''NOTE: READ THIS BEFORE CONTINUING

Below are a few simple examples of using the Calculus Object and its included functions. I've 
commented out the Plotly graphs to avoid having three browser tabs pop up at runtime. I am 
leaving it up to you (the user) to uncomment parts of this program and explore the features it
has to offer. Feel free to try it out and if you have any questions, shoot me an email at
dduval6@outlook.com'''
######################################################################################################

'''Set your Equation here'''
first_func = Calculus(x**2-1)
print(str(first_func) + '\n')
'''Set your domain here'''
print('Setting Domain from -10 to 10')
first_func.set_domain(list(range(-10, 11)))
print(first_func.get_domain())
'''Range is automatically set here based on x values (Domain)'''
print('\nSetting Range using the x values from the Domain -10 --> +10 inserted into the '+str(first_func))
first_func.set_range()
print(first_func.get_range())
'''Derivative is taken'''
print('\nTaking the derivative of the '+str(first_func))
print(first_func.take_derivative())
'''Integral is taken'''
print('\nTaking the integral of the '+str(first_func))
print(first_func.take_integral())
''' Substitute 35 for x in the funciton. It is then solved for the y value. (You give me an x, I give you a y!)'''
print('\nSolving the function with a number substituted for x:')
print(first_func.solvex(35))
print('\nSolving a definite integral from the x values -3 --> 4')
print(first_func.definite_integral(-3,4))


'''Plotting a graph of the function, the derivative of the function, and integral of the function.'''
# print('\nPlotting the original points...\n')
# first_func.plot_points()
# print('\nPlotting the derivative...\n')
# first_func.plot_derivative()
# print('\nPlotting the integral...\n')
# first_func.plot_integral()
