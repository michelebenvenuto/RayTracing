from usefullFunctions import V3
from Intersect import Intersect
from math import sqrt
from plane import Plane
from usefullFunctions import sum

class Cube(object):
    def __init__(self, center, material):
        self.center = center
        self.material = material
        self.cubeMins = V3(self.center.x - 0.5, self.center.y - 0.5, self.center.z - 0.5)
        self.cubeMax = V3(self.center.x + 0.5, self.center.y + 0.5, self.center.z + 0.5)
        self.planes = []

        self.planes.append( Plane(sum(center, V3(0.5,0,0) ) , V3(1,0,0), material) )
        self.planes.append( Plane(sum(center, V3(-0.5,0,0)) , V3(-1,0,0), material))

        self.planes.append( Plane(sum(center, V3(0,0.5,0)), V3(0,1,0),material))
        self.planes.append( Plane(sum(center, V3(0,-0.5,0)), V3(0,-1,0),material))

        self.planes.append( Plane(sum(center, V3(0,0,0.5)), V3(0,0,1), material))
        self.planes.append( Plane(sum(center, V3(0,0,-0.5)), V3(0,0,-1), material))

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
        
        return Intersect(
            distance= intersect.distance,
            point= intersect.point,
            normal= intersect.normal
        )

        # tx1 = (self.cubeMins.x - origin.x)/direction.x
        # tx2 = (self.cubeMax.x - origin.x)/direction.x

        # txExit = max(tx1, tx2)
        # txEnter = min(tx1, tx2)

        # ty1 = (self.cubeMins.y - origin.y)/direction.y
        # ty2 = (self.cubeMax.y - origin.y)/direction.y
        
        # tyExit = max(ty1, ty2)
        # tyEnter = min(ty1, ty2)

        # tz1 = (self.cubeMins.z - origin.z)/direction.z
        # tz2 = (self.cubeMax.z - origin.z)/direction.z
        
        # tzExit = max(tz1, tz2)
        # tzEnter = min(tz1, tz2)

        # tEnter = max(txEnter, tyEnter, tzEnter)
        # tExit = min(txExit, tyExit, tzExit)

        # if(tExit < tEnter):
        #     return None
        # else:
        #     point = V3(txExit, tyExit, tzExit)
        #     distance = ((point.x - origin.x)**2 +(point.y - origin.y)**2 +(point.z - origin.z)**2)**0.5
        #     if(tzEnter == tzEnter):
        #         return Intersect(
        #             distance= distance,
        #             point = point,
        #             normal= V3(0,0,1)
        #         )
            
        #     if(tyEnter == tEnter):
        #         return Intersect(
        #             distance= distance,
        #             point = point,
        #             normal= V3(0,1,0)
        #         )

        #     if(txEnter == tEnter):
        #         return Intersect(
        #             distance= distance,
        #             point = point,
        #             normal= V3(1,0,0)
        #         )