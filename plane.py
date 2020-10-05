from usefullFunctions import V3, sub, dot, length, mul, norm, sum,cross
from Intersect import Intersect
from math import sqrt
"""
Object used to describe a plane
B = upper right corner
C = lower left corner
"""
class Plane(object):
    def __init__(self, center, normal ,material):
        self.center = center
        self.normal = norm(normal)
        self.material = material

    def collisionDetected(self, origin, direction):
        denom = dot(direction, self.normal)

        if abs(denom) > 0.001:
            nom = dot(self.normal, sub(self.center, origin))
            t = nom/denom
            if t > 0:
                hit = sum(origin, V3(direction.x*t, direction.y*t, direction.z*t))
                if(hit.x> self.center.x +0.5 or hit.y> self.center.y +0.5 or hit.z> self.center.z +0.5 or hit.x< self.center.x -0.5 or hit.y< self.center.y -0.5 or hit.z< self.center.z -0.5 ):
                    return None
                return Intersect(
                    distance= t,
                    point = hit ,
                    normal = self.normal,
                )
        return None