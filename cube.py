from usefullFunctions import V3
from Intersect import Intersect
from math import sqrt
from plane import Plane
from usefullFunctions import sum

class Cube(object):
    def __init__(self, center, material, texture =None):
        self.center = center
        self.material = material
        self.texture = texture
        self.cubeMins = V3(self.center.x - 0.5, self.center.y - 0.5, self.center.z - 0.5)
        self.cubeMax = V3(self.center.x + 0.5, self.center.y + 0.5, self.center.z + 0.5)
        self.planes = []

        self.planes.append( Plane(sum(center, V3(0.5,0,0) ) , V3(1,0,0), material, texture) )
        self.planes.append( Plane(sum(center, V3(-0.5,0,0)) , V3(-1,0,0), material, texture))

        self.planes.append( Plane(sum(center, V3(0,0.5,0)), V3(0,1,0),material, texture))
        self.planes.append( Plane(sum(center, V3(0,-0.5,0)), V3(0,-1,0),material, texture))

        self.planes.append( Plane(sum(center, V3(0,0,0.5)), V3(0,0,1), material, texture))
        self.planes.append( Plane(sum(center, V3(0,0,-0.5)), V3(0,0,-1), material, texture))

    def collisionDetected(self, origin, direction):
        
        t = float('inf')
        intersect = None

        for plane in self.planes:
            planeIntersection = plane.collisionDetected(origin, direction)

            if planeIntersection is not None:
                if planeIntersection.point.x >= self.cubeMins.x and planeIntersection.point.x <= self.cubeMax.x:
                    if planeIntersection.point.y >= self.cubeMins.y and planeIntersection.point.y <= self.cubeMax.y:
                        if planeIntersection.point.z >= self.cubeMins.z and planeIntersection.point.z <= self.cubeMax.z:
                            if planeIntersection.distance < t:
                                t = planeIntersection.distance
                                intersect = planeIntersection
        if intersect is None:
            return None
        
        elif self.texture is None:
            return Intersect(
                distance= intersect.distance,
                point= intersect.point,
                normal= intersect.normal
            )

        else:
            return Intersect(
                distance= intersect.distance,
                point= intersect.point,
                normal= intersect.normal,
                texture_color= intersect.texture_color
            )