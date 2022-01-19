class Rack:
    rack = []
    
    def add(self, ball):
        self.rack.append(ball)
    
    def balls(self):
        rack = self.sort(self.rack)
        return self.rack

    def sort(self, rack):
        for i in range(0, (len(self.rack)-1)):
            if self.rack[i] < self.rack[i+1]:
                pass

        return rack


#have:
# 20, 10, 30
#  0,  1,  2

# want:
# 10, 20, 30
#  0,  1,  2