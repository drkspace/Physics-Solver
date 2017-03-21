from constants import PI
from decimal import Decimal as d
class shape(object):

    def __init__(self, shape, self.radius=d('0'), self.length=d('0'), self.width=d('0'), self.height=d('0')):
        self.shape=shape
        
        if self.shape=="SPHERE":
            self.area=d('4')*PI*self.radius**d('2')
            self.volume=d('4')*PI*(self.radius**d('3'))/d('3')

        elif self.shape == "PLATES":
            self.area=self.length*self.width
            
        elif self.shape == "CYLENDER":
            self.area=PI*self.radius*d('2')*self.length
            self.volume=PI*(self.radius**d('2'))*self.length

        
