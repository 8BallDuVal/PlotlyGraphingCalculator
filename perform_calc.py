'''
Created on Oct 3, 2018

@author: daduva
'''
'''
Created on Oct 3, 2018

@author: daduva
'''
from sympy import Symbol, Derivative, integrate
import math
import plotly.offline as ply 
import plotly.graph_objs as go
class Calculus:
    def __init__(self, function):
        self.function = function
        self.x_values = []
        self.y_values = []
    def take_derivative(self):
        x = Symbol('x')
        deriv= Derivative(self.function, x)
        return deriv.doit()
    def take_integral(self):
        x = Symbol('x')
        integral = integrate(self.function, x)
        return integral.doit()
    def definite_integral(self, *args):
        x = Symbol('x')
        return integrate(self.function, (x, args))
    def set_domain(self, range):
        self.x_values = range     
    def set_range(self):
        x = Symbol('x')
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
        x = Symbol('x')
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
        x = Symbol('x')
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
        x = Symbol('x')     
        return self.function.subs(x,variable)    
    def __repr__(self):
        return "Calculus('{}')".format(self.function)
    def __str__(self):
        return "Function: {}".format(self.function)  
    def __add__(self, other):
        return self.function + ' + ' + other.function
