from ray import RayTracer
from ray import White
from sphere import Sphere
from usefullFunctions import V3
from light import Light
from mats import *
from usefullFunctions import color

"""
NOTA: LAS MANCHAS NEGRAS QUE SE VEN EN EL RENDER SON LAS ESFERAS
PROYECTANDO SUS SOMBRAS  
"""

r = RayTracer(800, 800)

r.light = Light(
  position=V3(20, 20, 20),
  intensity=1.5
)

r.backgroundColor = color(50, 50, 200)

r.scene = [
  Sphere(V3(0, 0, -5), 0.45, christmasbulb),
  #head
  Sphere(V3(0, 0.5, -4.5), 0.25, brownfuzz),
  #ears
  Sphere(V3(-0.25, 0.7, -4.5), 0.15, darkbrown),
  Sphere(V3(0.25, 0.7, -4.5), 0.15, darkbrown),
  #eyes
  Sphere(V3(-0.1, 0.55, -4), 0.05, eyesout),
  Sphere(V3(0.1, 0.55, -4), 0.05, eyesout),
  Sphere(V3(-0.08, 0.52, -3.9), 0.025, eyesin),
  Sphere(V3(0.1, 0.52, -3.9), 0.025, eyesin),
  #nose
  Sphere(V3(0, 0.36, -3.4), 0.09, darkbrown),
  Sphere(V3(0, 0.35, -3.3), 0.025, eyesin),
  #arms
  Sphere(V3(0.5, 0, -5), 0.25, brownfuzz),
  Sphere(V3(-0.5, 0, -5), 0.25, brownfuzz),
  # #legs
  Sphere(V3(0.25, -0.5, -5), 0.25, brownfuzz),
  Sphere(V3(-0.25, -0.5, -5), 0.25, brownfuzz),
]
r.render()
r.glFinish()