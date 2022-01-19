class Rack:
    rack = []
    
    def add(self, ball):
        self.rack.append(ball)
    
    def balls(self):
        self.rack.sort()
        return self.rack