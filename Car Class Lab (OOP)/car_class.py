class Car(object):
    """This is a car class/blueprint for creating various car instances"""
    #Below is the constructor to set up instance variables
    def __init__(self, name='General', model='GM', car_type=None):
        self.speed = 0
        self.name = name
        self.model = model
        self.car_type = car_type
        if self.name is 'Porshe' or self.name is 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.car_type is 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
    
    #This method checks wether car_type is saloon        
    def is_saloon(self):
        if self.car_type is not 'trailer':
            self.car_type = 'saloon'
            return True
        return False
    
    #This method checks an instance moving speed and returns the instance    
    def drive(self, speed):
        self.speed = speed
        if self.name == 'MAN':
          self.speed = 77
          return self
        elif self.name == 'Mercedes':
          self.speed = 1000
          return self
        else:
          pass
