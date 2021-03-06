# PlotlyGraphingCalculator
Graph functions, take integrals/derivatives of those functions, and plot them on the same graph.

Written in Python 3.6.5 for Windows. Uses the Plotly API to create interactive graphs that open in a web browser.

Required packages:
- Sympy 1.1.1
- Plotly 3.2.0

The program was written using Object-Oriented Programming, and requires that you initialize a Calculus object with a function string.

Here's a quick example of initializing a Calculus object:

x = Symbol('x')****

function = Calculus(3*x**3-4)

The function variable is now considered a Calculus object, and you can use the program's methods to take derivatives, integrate, or plot the function.

****The x = Symbol('x') line is not necessary if the Calculus object is being created in the main perform_calc.py file. However, if you want to start a new python file and use the Calclulus object within that file, you must include the x = Symbol('x') line at the top of the file.

Here is a list of the included methods/functions:
- __init__ --> initializes the object with specific properties.
- __repr__ --> returns an easily readible representation of the object when you print an object variable to the console.
- __str__ --> similar to __repr__, this method simply returns the function of the object.
- __add__ --> allows you to 'add' together two object variable's functions in a string.
- take_derivative --> takes the derivative of a function, and returns the derivative.
- take_integral --> takes the integral of a function, and returns the integral.
- definite_integral --> takes a definite integral of a function (from one x value to x value)
- set_domain --> allows you to manually set the domain of a function.
- set_range --> after setting the domain, the range must be set using the domain values.
- get_domain --> returns the domain as a list
- get_range --> returns the range as a list
- solvex --> replaces the x variables in the equation with a number and solves it. 'You give me an x, I give you a y'.
- plot_points --> using the domain and range values, plot the points on an interactive graph (generated by the Plotly API)
- plot_derivative --> Plots the derivative function and original function on the same graph
- plot_integral --> plots the integral function and the original function on the same graph

********************************************************************************************************************************
Some notes about how to enter a function:
For this program, Python requires that you include an asterisk (*) in between each variable and number. To raise a variable to a power, you must use two asterisks (**). For example, if you wanted to enter the function:

6x^2+5x-3

You would have to make sure and enter it in as it is below to avoid any error messages: 
6*x**2+5*x-3

Also, if there are any fractions in the equation, make sure and include parentheses around the function like so:
(6*x**2-3)/(6*x**3-3)

If there are square roots in the function, use sqrt():
sqrt(6*x**2-3)/(9*x**2-4)

For Trigonometric functions, simply use cos(x), sin(x), tan(x), sec(x), csc(x), cot(x).

For more information on what syntax may or may not be accepted, visit https://docs.sympy.org/0.7.1/index.html
********************************************************************************************************************************
There is one python file included in this repository, perform_calc.py.

The perform_calc.py file is the main program file, which also includes some examples testing out what the program does and how it works (located at the very bottom of the perform_calc.py file). This can be ran directly in a python interpreter/command prompt window.
********************************************************************************************************************************

This is still a work in progress. Let me know if you have any questions/conerns!
