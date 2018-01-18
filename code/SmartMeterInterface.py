from Smart Meter Sensor import Smart Meter Sensor

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

class Smart Meter Pole():
    '''This is the pole for the Smart Meter'''

    def_init_ (self, n, wt, s)
        '''Intializes the pole'''
    self.name = n
    self.wireless transponder = wt
    self.sensor = s
    self.height = 5.0
    self.width = 2.0
    Pole.__init__(self, n, wt, s)