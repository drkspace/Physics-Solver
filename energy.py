import math
from constants import *
from particle import particle
from decimal import Decimal

#TODO
#part=particle(Decimal('10'))

#KENETIC <-> POTENTIAL

#If has height to Velocity
def KP_H_2_V(height):
    
    if type(height) is Decimal:
        return (Decimal('2')*g*height)**Decimal('.5')
    else:
        return

#velocity to height
def KP_V_2_H(velocity):
    if type(velocity) is Decimal:
        return velocity**Decimal('2')/(Decimal('2')*g)
    else:
        return
#Joules and mass to Velocity
def K_JM_2_V(joules, mass):
    if type(joules) is Decimal and type(mass) is Decimal:
        return (Decimal('2')*joules/mass)**Decimal('.5')
    else:
        return

