from ray import RayTracer
from ray import White
from sphere import Sphere
from usefullFunctions import V3
from mats import *

r = RayTracer(800,800)
r.scene  = [
    #EYES
    Sphere(V3(-5,-37,-100), 2, charcoal),
    Sphere(V3(5,-37,-100), 2, charcoal),
    #NOSE
    Sphere(V3(0,-32,-100), 2, orange),
    #MOUTH
    Sphere(V3(2,-25,-100), 2, charcoal),
    Sphere(V3(-2,-25,-100), 2, charcoal),
    Sphere(V3(5,-27,-100), 2, charcoal),
    Sphere(V3(-5,-27,-100), 2, charcoal),
    #UPPER BUTTONS 
    Sphere(V3(0,-10,-75), 2, charcoal),
    Sphere(V3(0,-5,-75), 2, charcoal),
    Sphere(V3(0,0,-75), 2, charcoal),
    Sphere(V3(0,5,-75), 2, charcoal),
    #LOWER BUTTONS
    Sphere(V3(0,15,-40), 2, charcoal),
    Sphere(V3(0,25,-40), 2, charcoal),
    #BODY
    Sphere(V3(0,2.5,-5), 2, snowWhite),
    Sphere(V3(0,0,-9), 2, snowWhite),
    Sphere(V3(0,-4,-13), 2, snowWhite),
    
]
r.render()
r.glFinish()