from decimal import Decimal
getcontext().prec=35
PI = Decimal('3.14159265358979323846264338327950288419716939937510582097')
E = Decimal('2.7182818284590452353602874713527')
G = Decimal('6.67408')*Decimal('10')**Decimal('-11')
g = Decimal('9.81')
MASS_PROTON = Decimal('1.67')*Decimal('10')**Decimal('-27')
MASS_NEUTRON = Decimal('1.67')*Decimal('10')**Decimal('-27')
MASS_ELECTRON = Decimal('9.11')*Decimal('10')**Decimal('-31')
CHARGE = Decimal('1.6')*Decimal('10')**Decimal('-19')
C = Decimal('3')*Decimal('10')**Decimal('8')
EPSILON_0 = Decimal('8.85')*Decimal('10')**Decimal('-12')
COULOMBS_CONSTANT = Decimal('1')/(Decimal('4')*PI*EPSILON_0)

