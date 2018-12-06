'''
Created on Oct 3, 2018

@author: daduva
'''
from sympy import *
import numpy as np
import math
import plotly.offline as ply 
import plotly.graph_objs as go
from sympy.solvers import solve

class Calculus:
    x_values = []
    y_values = []
    def __init__(self, function):
        self.x = Symbol('x')
        self.y = Symbol('y')
        self.z = Symbol('z')
        self.function = function

        if '^' in self.function:
            self.function = self.function.replace('^', '**')
    
    def take_derivative(self):
        deriv= Derivative(self.function, self.x)
        return str(deriv.doit())
    
    def take_integral(self):
        integral = integrate(self.function, self.x)
        return str(integral.doit())
    
    def definite_integral(self, *args):
        return integrate(self.function, args)
    
    def set_domain(self, range):
        self.x_values = range     
        
    def set_range(self):
        yvals = []
        self.y_values = np.array(yvals, dtype = np.float32)
        for x in self.x_values:
            try:
                yvals.append(float(eval(self.function)))
            except:
                yvals.append(math.inf)
        self.y_values = np.append(self.y_values, yvals)
        return self.y_values
    
    def get_domain(self):
        return self.x_values
    
    def get_range(self):
        return self.y_values
    
    def plot_points(self):
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Plot 1')
        data = [trace]
        ply.plot(data, filename = 'function-plot.html')
        
    def plot_derivative(self):
        derivative_xdomain = self.x_values.copy()
        yval_temp = []
        derivative_yrange =  np.array(yval_temp, dtype = np.float32)
        derivative_function = self.take_derivative()
        
        for x in derivative_xdomain:
            try:
                yval_temp.append(float(eval(str(derivative_function))))
            except:
                yval_temp.append(math.inf)
        derivative_yrange = np.append(derivative_yrange, yval_temp)
        
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Original Function')
        
        trace2 = go.Scatter(
            x = derivative_xdomain,
            y = derivative_yrange,
            mode = 'lines',
            name = 'Derivative Function')
        
        data = [trace, trace2]
        ply.plot(data, filename = 'function-plot.html')
        
    def plot_integral(self):
        integral_xdomain = self.x_values.copy()
        yval_temp = []
        integral_yrange =  np.array(yval_temp, dtype = np.float32)
        integral_function = self.take_integral()
        
        for x in integral_xdomain:
            try:
                yval_temp.append(float(eval(str(integral_function))))
            except:
                yval_temp.append(math.inf)
        integral_yrange = np.append(integral_yrange, yval_temp)
        
        trace = go.Scatter(
            x = self.x_values,
            y = self.y_values,
            mode = 'lines',
            name = 'Original Function')
        
        trace2 = go.Scatter(
            x = integral_xdomain,
            y = integral_yrange,
            mode = 'lines',
            name = 'integral Function')
        
        data = [trace, trace2]
        ply.plot(data, filename = 'function-plot.html')
    
    def solve_for(self, variable):     
        return solve(self.function, variable)      
    
    def __repr__(self):
        return "Calculus('{}')".format(self.function)
    
    def __str__(self):
        return "Function: {}".format(self.function)
    
    def __add__(self, other):
        return self.function + ' + ' + other.function
