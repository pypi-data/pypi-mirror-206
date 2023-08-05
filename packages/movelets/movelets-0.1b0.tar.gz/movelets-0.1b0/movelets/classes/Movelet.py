import movelets.classes as classes
# ------------------------------------------------------------------------------------------------------------
# MOVELETS 
# ------------------------------------------------------------------------------------------------------------
class Movelet(classes.Subtrajectory):
    def __init__(self, mid, tid, points, quality, label, start, size, children=None):
        super().__init__(mid, tid, points, label, start, size, children)
        self.quality = quality
        
    def toString(self):
        return str(self) + ' ('+'{:3.2f}'.format(self.quality)+'%)'    
    
    def diffToString(self, mov2):
        dd = self.diffPairs(mov2)
        return ' >> '.join(list(map(lambda x: str(x), dd))) + ' ('+'{:3.2f}'.format(self.quality)+'%)' 
        
    def toText(self):
        return ' >> '.join(list(map(lambda y: "\n".join(list(map(lambda x: "{}: {}".format(x[0], x[1]), x.items()))), self.data))) \
                    + '\n('+'{:3.2f}'.format(self.quality)+'%)'