from usefullFunctions import *
from math import sin, cos, tan, pi
from sphere import Sphere
from light import Light

White = color(255,255,255)
Black = color(0,0,0)

MAX_RECURSION_DEPTH = 3

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
        self.backgroundColor = Black
        self.light = Light(V3(0,0,0), 1)
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
        self.clearColor = color(r,g,b)

    def glVertex(self,x,y):
        XCoordinate = round((x+1)*(self.viewport.width/2)+self.viewport.x)
        YCoordinate = round((y+1)*(self.viewport.height/2)+self.viewport.y)
        self.point(XCoordinate,YCoordinate)

    def glColor(self, r,g,b):
        self.drawColor = color(r,g,b)

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
                f.write(self.pixels[y][x].toBytes())

        f.close()

    def point(self,x, y,color = None):
        try:
            self.pixels[y][x] = color or self.drawColor
        except:
            pass
    
    def collisionDetected(self, origin, direction):
        zbuffer = float('inf')

        material = None
        intersect = None
        for obj in self.scene:
            hit = obj.collisionDetected(origin,direction)
        
            if hit and hit.distance < zbuffer:
                zbuffer = hit.distance
                material = obj.material
                intersect = hit
        return material, intersect


    def cast_ray(self, origin, direction, recursion = 0):
        material_detected, impact = self.collisionDetected(origin,direction)
        

        #nothing got hit on any iteration 
        if material_detected is None or recursion>= MAX_RECURSION_DEPTH :
            return self.backgroundColor
        
        #light stuff

        light_direction = norm(sub(self.light.position, impact.point))
        light_distance = length(sub(self.light.position, impact.point))

        #shadow stuff
        offset_normal = mul(impact.normal, 1.1)

        shadow_origin = sub(impact.point, offset_normal) if dot(light_direction, impact.normal) < 0 else sum(impact.point, offset_normal)
        shadow_material, shadow_intersect = self.collisionDetected(shadow_origin, light_direction)
        shadow_intensity = 0

        if shadow_material and length(sub(shadow_intersect.point, shadow_origin)) < light_distance :
            shadow_intensity = 0.9

        intensity =self.light.intensity * max(0,dot(light_direction, impact.normal)) * (1- shadow_intensity)

        reflection = reflect(light_direction, impact.normal)
        specular_intensity = self.light.intensity * (
            max(0, -dot(reflection,direction))**material_detected.specular
        )

        #reflexion stuff
        if material_detected.albedo[2] > 0:
            reflect_dir = reflect(direction, impact.normal)
            reflect_orig = sub(impact.point, offset_normal) if dot(reflect_dir, impact.normal)< 0 else sum(impact.point, offset_normal)
            reflected_color = self.cast_ray(reflect_orig, reflect_dir, recursion + 1)
        else:
            reflected_color = Black

        # refraction stuff
        if material_detected.albedo[3] > 0:
            refract_dir = refract(direction, impact.normal, material_detected.refractive_index)
            refract_orig = sub(impact.point, offset_normal) if dot(refract_dir, impact.normal)< 0 else sum(impact.poin, offset_normal)
            refract_color = self.cast_ray(refract_orig, refract_dir, recursion + 1)
        else:
            refract_color = Black


        #Finall steps
        diffuse = material_detected.diffuse * intensity * material_detected.albedo[0]
        specular = color(255,255,255) * specular_intensity * material_detected.albedo[1]
        reflected = reflected_color * material_detected.albedo[2]
        refraction = refract_color * material_detected.albedo[3]

        return diffuse + specular + reflected + refraction

    def render(self):
        fov = int(pi/2)

        for y in range(self.height):
            for x in range(self.width):
                i = (2*(x + 0.5)/self.width - 1)* self.width/self.height *tan(fov/2)
                j = (2*(y + 0.5)/self.height - 1) * tan(fov/2)

                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)

#This class will be helpfull if more viewports are required in the future
class Viewport(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width