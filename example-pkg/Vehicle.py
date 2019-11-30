class Vehicle():
    def __init__(self, name, vtype, color, speed):
        self.name = name
        self.type = vtype
        self.color = color
        self.speed = speed

    def start(self):
        return 'Vehicle started'

    def stop(self):
        return 'Vehicle stopped'

    
