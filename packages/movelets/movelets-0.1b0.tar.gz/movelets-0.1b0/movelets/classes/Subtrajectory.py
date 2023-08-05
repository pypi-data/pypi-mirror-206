# ------------------------------------------------------------------------------------------------------------
# SUBTRAJECTORIES 
# ------------------------------------------------------------------------------------------------------------
class Subtrajectory:
    def __init__(self, mid, tid, points, label, start, size, children=None):
        self.mid     = mid
        self.tid     = tid
        self.label   = label
        self.start   = start
        self.size    = size
        
        self.data     = []
        if points is not None:
            list(map(lambda point: self.add_point(point), points))
                
    def __repr__(self):
        return '=>'.join([str(x) for x in self.data])
    def __hash__(self):
        return hash(self.__repr__())
    def __eq__(self, other):
        if isinstance(other, Movelet):
            return self.__hash__() == other.__hash__()
        else:
            return False
                
    def attributes(self):
        return self.data[0].keys()
    
    def add_point(self, point):
        assert isinstance(point, dict)
        self.data.append(self.point_dict(point))
        
    def point_dict(self, point):
        assert isinstance(point, dict)
        points = {}    
        
        def getKV(k,v):
            px = {}
            if isinstance(v, dict):
                if k == 'lat_lon' or k == 'space':
                    px['lat'] = v['x']
                    px['lon'] = v['y']
                else:
                    px[k] = v['value']
            else:
                if k == 'lat_lon' or k == 'space':
                    v = v.split(' ')
                    px['lat'] = v[0]
                    px['lon'] = v[1]
                elif k == 'space3d':
                    v = v.split(' ')
                    px['x'] = v[0]
                    px['y'] = v[1]
                    px['z'] = v[2]
                else:
                    px[k] = v
            return px
        
        list(map(lambda x: points.update(getKV(x[0], x[1])), point.items()))
                
        return points
        
    def toString(self):
        return str(self)   
    
    def diffToString(self, mov2):
        dd = self.diffPairs(mov2)
        return ' >> '.join(list(map(lambda x: str(x), dd)))
        
    def toText(self):
        return ' >> '.join(list(map(lambda y: "\n".join(list(map(lambda x: "{}: {}".format(x[0], x[1]), x.items()))), self.data)))
    
    def commonPairs(self, mov2):
        common_pairs = set()
        
        for dictionary1 in self.data:
            for dictionary2 in mov2.data:
                for key in dictionary1:
                    if (key in dictionary2 and dictionary1[key] == dictionary2[key]):
                        common_pairs.add( (key, dictionary1[key]) )
                        
        return common_pairs
      
    def diffPairs(self, mov2):
        diff_pairs = [dict() for x in range(self.size)]
        
        for x in range(self.size):
            dictionary1 = self.data[x]
            for dictionary2 in mov2.data:
                for key in dictionary1:
                    if (key not in dictionary2):
                        diff_pairs[x][key] = dictionary1[key]
                    elif (key in dictionary2 and dictionary1[key] != dictionary2[key]):
                        diff_pairs[x][key] = dictionary1[key]
                    elif (key in dictionary2 and key in diff_pairs[x] and dictionary1[key] == dictionary2[key]):
                        del diff_pairs[x][key]
                        
        return diff_pairs