from usefullFunctions import *
from math import sin, cos, tan, pi
from sphere import Sphere

White = getcolor(255,255,255)
Black = getcolor(0,0,0)

class RayTracer(object):
    def __init__(self, width, height, fileName = 'test.bmp', clearColor = Black):
        self.width = width
        self.height = height
        self.fileName = fileName
        self.clearColor = clearColor
        self.pixels = []
        self.scene = []
        self.viewport = None
        self.drawColor = White
        self.active_texture = None
        self.active_vertex_array = []
        self.glCreateWindow(self.width,self.height)
        
    def glInit(self):
        return('TODO')

    def glCreateWindow(self,width,height):
        self.pixels = [
            [self.clearColor for x in range(width)]
            for y in range(height) 
        ]
        self.zbuffer = [
            [-float('inf') for x in range(self.width)]
            for y in range(self.height)
        ]

    def glViewPort(self,x,y, width, height):
        self.viewport = Viewport(x,y,height,width)
    
    def glClear(self):
        self.pixels = [
            [self.clearColor for x in range(self.width)]
            for y in range(self.height) 
        ]
    
    def glClearColor(self, r,g,b):
        self.clearColor = getcolor(r,g,b)

    def glVertex(self,x,y):
        XCoordinate = round((x+1)*(self.viewport.width/2)+self.viewport.x)
        YCoordinate = round((y+1)*(self.viewport.height/2)+self.viewport.y)
        self.point(XCoordinate,YCoordinate)

    def glColor(self, r,g,b):
        self.drawColor = getcolor(r,g,b)

    def glFinish(self):
        f = open(self.fileName, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(14 + 40 ))

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for y in range(self.height):
            for x in range(self.width):
                f.write(self.pixels[y][x])

        f.close()

    def point(self,x, y,color = None):
        try:
            self.pixels[y][x] = color or self.drawColor
        except:
            pass
    
    def collisionDetected(self, origin, direction):
        for obj in self.scene:
            if obj.collisionDetected(origin, direction):
                return obj.material.diffuse
        return False


    def cast_ray(self, origin, direction):
        material_detected = self.collisionDetected(origin,direction)
        if material_detected:
            return material_detected
        else:
            return Black

    def render(self):
        fov = pi/2
        for y in range(self.height):
            for x in range(self.width):
                i = (2*(x + 0.5)/self.width - 1)* self.width/self.height *tan(fov/2)
                j = -(2*(y + 0.5)/self.height - 1) * tan(fov/2)

                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)

#This class will be helpfull if more viewports are required in the future
class Viewport(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width