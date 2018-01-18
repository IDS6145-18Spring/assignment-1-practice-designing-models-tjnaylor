## This is code for the Smart Meter. It describes how the Smart Meter collects information from sensors throughout the city and provide that information to drivers.
## This particular page focus on  the digital interface.
## The digital interface is the first physical part of the Smart Meter that users interacts with and must provide features that computes the time of day, time of use by the user, links to payment options and displays charge level.

From Smart Meter Sensor import Smart Meter Sensor
class Smart Meter Interface ():
      ''' This is the digital interface'''

    def_init_(self, n, d, l, wt, s, p, t, c):
        '''Intializes the Smart Meter'''
    self.name = n
    self.digital display = d
    self.light = l
    self.wireless transponder = wt
    self.sensor = s
    self.payment = p
    self.time = t
    self.charge = c
    self.height= 2.0
    self. width= 2.0
    Interface.__init__(self, n, d, l, wt, s, p, t, c)

From Smart Meter Interface import Smart Meter Interface
From Smart Meter Sensor import Smart Meter Sensor
class Smart Meter Payment System():

    def_init_(self, n, p, co, r, wt)
    '''Initializes payment for the Smart Meter'''
    self.name = n
    self.payment = p
    self.coin = co
    self.wireless transponder = wt
    self.receipt = r
    payment._init_(self, n, p, co, r, wt)

class Smart Meter Pole():
    '''This is the pole for the Smart Meter'''

    def_init_ (self, n, wt, s)
        '''Intializes the pole'''
    self.name = n
    self.wireless transponder = wt