''' Circuitous(tm)                              # Give the project a name
An Advanced Circle Analytics                    # Elevator Pitch -> What problem you solve and how you solve it
'''

# New-style classes inherit from object
# Inheritance is a tool for code re-use. It allows one class to reuse the code from another.
# object() has a __getattribute__ method that provides a reprogrammable dot.
# Python pgorammers tend to document first.
# 1) It better defines the problem, makeing it more solvable.
# 2) There is an immediate payoff with help(), pydoc, sphinx, tooltip, etc
# Give names to "magic constants". Second benefit is maing the value consistent in the module.
# D.R.Y. : Do not Repeat Yourself. is a code smell.
# Code Smell: Code that works but is awkward to understand or maintain
# Indicates a need to refactor
# Constants should have uppercase variable names
# M.V.P. -- Minimum Viable Product
# YANGI,RT -- You ain't gonna need it right now
# "Dogfooding" -- Eat your own dogfood --> Be your own first user.Alpha

import math
from collections import namedtuple

Version = namedtuple('Version',['major','minor','micro'])

class Circle(object):
    version = Version(0,1,1)       # Class variables are shared by all instance and visible 
    
    'Advanced circle analytic toolkit'
    # The use of "self" is a cultural norm
    # Parameter names are user visible, part of the API and should be spelled-out.
    # Spelling-out avoids cultural bias for abbreviations.
    # When copying from one namespace to another, we generaaly keep the name the same. 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        'Perform quadrature on a planar shape of uniform revolution'
        return math.pi * self.radius**2.0