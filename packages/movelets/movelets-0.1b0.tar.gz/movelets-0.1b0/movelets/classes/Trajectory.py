# ------------------------------------------------------------------------------------------------------------
# TRAJECTORY 
# ------------------------------------------------------------------------------------------------------------
class Trajectory:
    def __init__(self, tid, label, attributes, new_points, size):
        self.tid          = tid
        self.label        = label
        self.attributes   = []
        self.size         = size
        
        for attr in attributes:
            if (attr == 'lat_lon' or attr == 'space') and 'lat' not in self.attributes:
                self.attributes.append('lat')
                self.attributes.append('lon')
            else:
                self.attributes.append(attr)
        
        self.points       = []
        if new_points is not None:
            self.points = list(map(lambda point: self.point_dict(point), new_points))
                
    def __repr__(self):
        return '=>'.join([str(x) for x in self.points])
    def __hash__(self):
        return hash(self.__repr__())
    def __eq__(self, other):
        if isinstance(other, Movelet):
            return self.__hash__() == other.__hash__()
        else:
            return False
                
    def add_point(self, point):
        assert isinstance(point, dict)
        self.points.append(self.point_dict(px))
        
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
        
            #if isinstance(v, dict):
            #    if k == 'lat_lon' or k == 'space':
            #        px['lat'] = v['x']
            #        px['lon'] = v['y']
            #    else:
            #        px[k] = v['value']
            #else:
            #    if k == 'lat_lon' or k == 'space':
            #        v = v.split(' ')
            #        px['lat'] = v[0]
            #        px['lon'] = v[1]
            #    elif k == 'space3d':
            #        v = v.split(' ')
            #        px['x'] = v[0]
            #        px['y'] = v[1]
            #        px['z'] = v[2]
            #    else:
            #        px[k] = v
            #        
#         self.points.append(point)
        
    def toString(self):
        return str(self)
        
    def toText(self):
        return ' >> '.join(list(map(lambda y: "\n".join(list(map(lambda x: "{}: {}".format(x[0], x[1]), y.items()))), self.points)))
    
    def points_trans(self):
        pts_trans = []
        def trans(attr):
        #for attr in self.attributes:
            col = {}
            col['attr'] = attr
            for i in range(self.size):
                col['p'+str(i)] = self.points[i][attr]
            return col
            #pts_trans.append(col)

        pts_trans = list(map(lambda attr: trans(attr), self.attributes))
        return pts_trans