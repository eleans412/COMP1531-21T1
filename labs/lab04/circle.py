import math

class Circle:
    '''
    Takes input as radius and outputs circumference and area of a circle

    Parameters:
        c (int): The radius

    Returns:
        Circumference (float): circumference of a circle with c as the radius
        Area (float): area of a circule with c as the radius
    '''
    def __init__(self, c):
        self.c = c
        
        if self.c < 0:
            raise Exception('Invalid input. Input needs to be positive number')
        #raise Exception('Invalid input. Input needs to be positive number')
        #square_radius = pow(self.c, 2)
        #self.area = square_radius * math.pi
        #self.circumference = 2 * c * math.pi

    def area(self):
        return self.c**2*math.pi

    def circumference(self):
        #if self.c < 0:
            #raise Exception('Invalid input. Input needs to be positive number')
        return 2*self.c*math.pi
	
	
