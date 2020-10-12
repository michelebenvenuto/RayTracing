from usefullFunctions import V3, sub, dot, length, mul, norm, sum,cross
from Intersect import Intersect
from math import sqrt
"""
Object used to describe a plane
B = upper right corner
C = lower left corner
"""
class Plane(object):
    def __init__(self, center, normal ,material, texture = None):
        self.center = center
        self.normal = norm(normal)
        self.material = material
        self.texture = texture

    def collisionDetected(self, origin, direction):
        denom = dot(direction, self.normal)

        if abs(denom) > 0.001:
            nom = dot(self.normal, sub(self.center, origin))
            t = nom/denom
            if t > 0:
                hit = sum(origin, V3(direction.x*t, direction.y*t, direction.z*t))
                if(hit.x> self.center.x +0.5 or hit.y> self.center.y +0.5 or hit.z> self.center.z +0.5 or hit.x< self.center.x -0.5 or hit.y< self.center.y -0.5 or hit.z< self.center.z -0.5 ):
                    return None
                elif self.texture is None:
                    return Intersect(
                        distance= t,
                        point = hit ,
                        normal = self.normal,
                    )
                else:
                    if abs(hit.x) == 1:
                        u = (hit.z - self.center.z + 0.5) 
                        v = (hit.y - self.center.y + 0.5)
                    elif abs(hit.y) == 1:
                        u = (hit.x - self.center.x + 0.5) 
                        v = (hit.z - self.center.z + 0.5) 
                    else:
                        u = (hit.x - self.center.x + 0.5) 
                        v = (hit.y - self.center.y + 0.5) 
 
                    return Intersect(
                        distance= t,
                        point = hit ,
                        normal = self.normal,
                        texture_color= self.texture.getColor(u,v)
                    )

        return None