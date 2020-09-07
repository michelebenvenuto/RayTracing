from ray import RayTracer
from ray import White
from sphere import Sphere
from usefullFunctions import V3
from mats import *

r = RayTracer(800,800)
r.scene  = [
    #EYES
    Sphere(V3(-5,-35,-100), 2, charcoal),
    Sphere(V3(5,-35,-100), 2, charcoal),
    #NOSE
    Sphere(V3(0,-30,-100), 2, orange),
    #MOUTH
    Sphere(V3(2,-23,-100), 2, charcoal),
    Sphere(V3(-2,-23,-100), 2, charcoal),
    Sphere(V3(5,-25,-100), 2, charcoal),
    Sphere(V3(-5,-25,-100), 2, charcoal),
    #UPPER BUTTONS 
    Sphere(V3(0,-10,-75), 2, charcoal),
    Sphere(V3(0,-5,-75), 2, charcoal),
    Sphere(V3(0,0,-75), 2, charcoal),
    Sphere(V3(0,5,-75), 2, charcoal),
    #LOWER BUTTONS
    Sphere(V3(0,10,-40), 2, charcoal),
    Sphere(V3(0,20,-40), 2, charcoal),
    #BODY
    Sphere(V3(0,2.5,-7), 2, snowWhite),
    Sphere(V3(0,0,-11), 2, snowWhite),
    Sphere(V3(0,-4,-15), 2, snowWhite),
    
]
r.render()
r.glFinish()